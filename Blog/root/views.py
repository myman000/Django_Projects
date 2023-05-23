from django.shortcuts import render
from .models import Blog

# Create your views here.

def home(request,slider_blog_id):
    slider_blog_id = int(slider_blog_id)
    print(slider_blog_id)
    data = Blog.objects.get(id=slider_blog_id)
    return render(request=request,template_name='root/home.html',context={'data':data})