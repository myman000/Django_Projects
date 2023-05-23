from django.shortcuts import render

# Create your views here.

def home(request):
    context = {'home':'active'}
    return render(request,'root/home.html',context)