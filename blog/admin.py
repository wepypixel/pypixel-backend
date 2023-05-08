from django.contrib import admin
from .models import BlogPost, Category, AboutUs
# Register your models here.

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Category)
admin.site.register(AboutUs)
