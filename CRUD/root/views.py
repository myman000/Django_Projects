from django.shortcuts import render,HttpResponseRedirect
from .forms import Register
from .models import Student
# Create your views here.


def home(request):
    if request.method == 'POST':
        fm = Register(request.POST)
        if fm.is_valid():
            fm.save()
            data = Student.objects.all()
    else:
        fm = Register()
        data = Student.objects.all()
    return render(request,'root/home.html',{'form':fm,'data':data})


def delete(request,id):
    data = Student.objects.get(pk = id)
    data.delete()
    return HttpResponseRedirect('/')


def Update(request,id):
    if request.method == 'POST':
        data = Student.objects.get(pk = id)
        fm = Register(request.POST,instance=data)
        if fm.is_valid():
            fm.save()
    else:
        data = Student.objects.get(pk = id)
        fm = Register(instance=data)
    return render(request,'root/update.html',{'form':fm})