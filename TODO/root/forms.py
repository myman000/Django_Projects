from django import forms
from .models import Task
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_Name', 'dateTime', 'priority']
        widgets = {'dateTime': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
                   'task_Name': forms.TextInput(attrs={'placeholder': 'Add New Task', 'class': 'form-control'}), 'priority': forms.Select(attrs={'class': 'form-select'}, choices=(('Medium','Priority'),('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')))}


# User Registeration Form

class RegisterForm(UserCreationForm):
    password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'placeholder': 'password'}))
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'placeholder': 'password(confirm)'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'username': forms.TextInput(attrs={'placeholder': 'username'}),
            'email': forms.TextInput(attrs={'placeholder': 'example@gmail.com'})
        }
