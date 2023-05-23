from django.shortcuts import render

# Create your views here.

def ContactView(request):
    return render(request,'myself/contact.html')