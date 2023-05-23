from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterCustomeForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email')

class AdminRegisterCustomeForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'