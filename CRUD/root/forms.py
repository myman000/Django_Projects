from django import forms
from .models import Student
class Register(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('first_name','last_name','email','department','dob')

        widgets = {'first_name':forms.TextInput(attrs={'class':'form-control'}),
        'last_name':forms.TextInput(attrs={'class':'form-control'}),
        'email':forms.EmailInput(attrs={'class':'form-control'}),
        'department':forms.TextInput(attrs={'class':'form-control'}),
        'dob':forms.DateInput(attrs={'class':'form-control'}),}