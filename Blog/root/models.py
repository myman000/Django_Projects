from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, max_length=100)

    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

class Subcategory(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Subcategories'

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30, unique=True)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=500, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE,default=None)
    main_image = models.ImageField(upload_to='images/')
    overview = models.TextField(max_length=300,default='There is nothing to show')
    content = models.TextField()
    tags = models.ManyToManyField('Tag', blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)
    status = models.CharField(max_length=10, choices=[('draft', _('Draft')), ('publish', _('Publish'))], default='draft')

    class Meta:
        ordering = ['-created_on']
    
    def is_published(self):
        return self.status == 'publish'
    is_published.boolean = True
    is_published.short_description = 'Published?'