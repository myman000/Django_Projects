from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from .forms import RegisterForm,TaskForm
from .models import Task
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
# Create your views here.

# Task View

def Test(request):
    return render(request,'root/base.html')

def Home(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = TaskForm(request.POST)
            data = Task.objects.filter(user=request.user).order_by('dateTime')
            if fm.is_valid():
                username = request.user
                task = fm.cleaned_data.get('task_Name')
                datetime = fm.cleaned_data.get('dateTime')
                priority = fm.cleaned_data.get('priority')
                reg = Task(user = username, task_Name = task,dateTime=datetime,priority = priority)
                reg.save()
        
        else:
            fm = TaskForm()
            data = Task.objects.filter(user=request.user).order_by('dateTime')
        
        return render(request,'root/home.html',{'form':fm,'data':data})
    
    else:
        return HttpResponseRedirect('/login/')



def updateTaskView(request,pk):
    if request.user.is_authenticated:
        data = Task.objects.get(id=pk)
        print(data.id)
        if request.user == data.user and data.id == pk:
            if request.method == 'POST':
                fm = TaskForm(request.POST, instance=data)
                if fm.is_valid():
                    username = request.user
                    task = fm.cleaned_data.get('task_Name')
                    datetime = fm.cleaned_data.get('dateTime')
                    priority = fm.cleaned_data.get('priority')
                    reg = Task(id = pk,user = username, task_Name = task,dateTime = datetime,priority = priority)
                    reg.save()
                    messages.success(request,'Successfuly updated the list!')
                    return HttpResponseRedirect('/')
            else:
                fm = TaskForm(instance=data)
            return render(request,'root/update.html',{'form':fm})
        else:
            return HttpResponse('Bad Request')
    else:
        return HttpResponseRedirect('/login/')


def deleteTaskView(request,pk):
    if request.user.is_authenticated:
        data = Task.objects.get(id=pk)
        if request.user == data.user and data.id == pk:
            data.delete()
            messages.success(request, 'Successfuly Deleted The Task!')
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('Bad Request')
    else:
        return HttpResponseRedirect('/login/')




# User Registeration View

def RegisterView(request):
    if request.method == 'POST':
        fm = RegisterForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'You are now family!!')
    
    else:
        fm = RegisterForm()
    
    return render(request,'root/register.html',{'form':fm})


# User Login View

def LoginView(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data = request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data.get('username')
                upass = fm.cleaned_data.get('password')
                user = authenticate(username = uname, password = upass)
                if user is not None:
                    login(request,user)
                    messages.success(request, 'Successfuly Logged In!!')
                    return HttpResponseRedirect('/')
            else:
                messages.error(request,'Username or password is incorret!')
                return HttpResponseRedirect('/login/')
    
        else:
            fm = AuthenticationForm()
            return render(request,'root/login.html',{'form':fm})
    
    else:
        return HttpResponseRedirect('/')


# User Logout View

def LogoutView(request):
    if request.user.is_authenticated:
        logout(request=request)
        messages.success(request,'Successfuly Logged Out!')
        return HttpResponseRedirect('/login/')
    else:
        return HttpResponseRedirect('/login/')

