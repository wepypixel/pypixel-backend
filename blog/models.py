from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=150)
    category_image = models.ImageField(upload_to='category_image/')
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

    
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    cover_image = models.ImageField(upload_to ='coverimage/')
    meta_description = models.CharField(max_length=120)
    content = RichTextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    view_count = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="category")


    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class AboutUs(models.Model):
    title = models.CharField(max_length=100)
    about_us_image = models.ImageField(upload_to='about-us')
    content = RichTextField()

    class Meta:
        verbose_name_plural = "About Us"

    def __str__(self):
        return self.title



class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    class Meta:
        verbose_name_plural = "Contact Us"
    
    def __str__(self):
        return self.name