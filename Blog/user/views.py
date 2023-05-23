from django.shortcuts import render,HttpResponseRedirect
from .forms import RegisterCustomeForm,AdminRegisterCustomeForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def RegisterView(request):
    if request.method == 'POST':
        fm = RegisterCustomeForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = RegisterCustomeForm()
    return render(request,'user/register.html',{'form':fm})

def AdminRegisterView(request):
    if request.method == 'POST':
        fm = AdminRegisterCustomeForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = AdminRegisterCustomeForm()
    return render(request,'user/register.html',{'form':fm})

def LoginView(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request,data = request.POST)
            if fm.is_valid():
                user_name = fm.cleaned_data.get('username')
                user_password = fm.cleaned_data.get('password')
                user = authenticate(username = user_name, password = user_password)
                if user is not None:
                    login(request=request,user=user)
                    return HttpResponseRedirect('/')
        else:
            fm = AuthenticationForm()
        return render(request,'user/login.html',{'form':fm})
    else:
        return HttpResponseRedirect('/')

def LogoutView(request):
    logout(request)
    return HttpResponseRedirect('/user/login/')