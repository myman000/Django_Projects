from django.contrib import admin
from .models import Blog,Category,Subcategory,Tag

# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','title','slug','author','category','subcategory','main_image','created_on','updated_on','status')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name','slug')

@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name','slug','category')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id','name','slug')