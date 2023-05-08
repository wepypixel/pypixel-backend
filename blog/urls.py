from django.urls import path
from .views import *

urlpatterns = [
    path('api/recentposts/', RecentPostListAPIView.as_view(), name='recent_post_list_api'),
    path('api/posts', PostListAPIView.as_view(), name='post_list_api'),
    path('api/post/<slug:slug>/', PostDetailAPIView.as_view(), name='post-detail'),
    path('api/category/<str:str>', CategoryPostsView.as_view(), name='category_post_list_api'),
    path('api/about-us', AboutUsAPIView.as_view(), name='about_us_api'),
    path('api/categories', CategoryAPIView.as_view(), name='category_api'),
    path('api/popular/<str:str>', PopularCategoryPostsView.as_view(), name='popular_category_post_list_api'),
    path('api/blog-posts/search/', BlogPostSearchView.as_view(), name='search_api'),
    
    # path('api/contactus/', ContactUsView.as_view(), name='contact_us_api'),
]