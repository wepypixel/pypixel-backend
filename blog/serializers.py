from rest_framework import serializers
from .models import BlogPost, Category, AboutUs, ContactUs
from django.conf import settings

class CategorySerializer(serializers.ModelSerializer):
    
    category_image = serializers.ImageField(use_url=False)

    class Meta:
      model = Category
      fields = '__all__'

class PostSerializer(serializers.ModelSerializer):    
    cover_image = serializers.ImageField(use_url=False)
    category = CategorySerializer()

    class Meta:
        model = BlogPost
        fields = '__all__'


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'subject', 'message']