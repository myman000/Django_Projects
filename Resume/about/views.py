from django.shortcuts import render

# Create your views here.


def Contact(request):
    context = {'contact':'active'}
    return render(request,'about/contact.html',context)