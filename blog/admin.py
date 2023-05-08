from django.contrib import admin
from .models import BlogPost, Category, AboutUs, ContactUs
# Register your models here.

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject')

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Category)
admin.site.register(AboutUs)
admin.site.register(ContactUs, ContactUsAdmin)
