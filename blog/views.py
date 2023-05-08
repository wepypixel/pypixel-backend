from rest_framework import generics
from .models import BlogPost, AboutUs, Category
from .serializers import PostSerializer, AboutUsSerializer, CategorySerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter
from django.conf import settings
from rest_framework import status


class MyModelPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'current_page': self.page.number,
            'total_pages': self.page.paginator.num_pages,
            'results': data
        })
    

class PostListAPIView(APIView):
    def get(self, request):
        queryset = BlogPost.objects.all()
        paginator = MyModelPagination()
        results = paginator.paginate_queryset(queryset, request)
        serializer = PostSerializer(results, many=True)
        for post in serializer.data:
            post['cover_image'] = settings.MEDIA_URL + post['cover_image']
        return paginator.get_paginated_response(serializer.data)
    
class RecentPostListAPIView(generics.ListAPIView):
    queryset = BlogPost.objects.order_by('-created_on')[:3]
    serializer_class = PostSerializer
    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        for post in response.data:
            post['cover_image'] = settings.MEDIA_URL + post['cover_image']
        return response
    

class PostDetailAPIView(generics.RetrieveAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        data['cover_image'] = settings.MEDIA_URL + data['cover_image']
        return Response(data)
    
class CategoryPostsView(generics.ListAPIView):
    serializer_class = PostSerializer
    pagination_class = MyModelPagination

    def get_queryset(self):
        category_name = self.kwargs['str'].capitalize()
        queryset = BlogPost.objects.filter(category__name=category_name).all()
        for post in queryset:
            post.cover_image = settings.MEDIA_URL +str(post.cover_image)
        
        return queryset
    
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
        
class AboutUsAPIView(APIView):
    def get(self, request):
        try:
            about_us = AboutUs.objects.get()
        except AboutUs.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = AboutUsSerializer(about_us)
        return Response(serializer.data)
    
class CategoryAPIView(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = Category.objects.all()
        for category in queryset:
            category.category_image = settings.MEDIA_URL +str(category.category_image)
        
        return queryset

class PopularCategoryPostsView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        category_name = self.kwargs['str'].capitalize()
        queryset = BlogPost.objects.filter(category__name=category_name).all().order_by('-view_count')[:12]
        for post in queryset:
            post.cover_image = settings.MEDIA_URL +str(post.cover_image)
        
        return queryset


class BlogPostSearchView(generics.ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = PostSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'content']
    pagination_class = MyModelPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.extra(select={'cover_image':  "'{0}' || cover_image".format(settings.MEDIA_URL)})
        return queryset

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)