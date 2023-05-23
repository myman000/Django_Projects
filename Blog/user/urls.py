from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.RegisterView,name = 'regiter'),
    path('adminregister/',views.AdminRegisterView,name = 'adminRegister'),
    path('login/',views.LoginView,name = 'login'),
    path('logout/',views.LogoutView, name = 'logout'),
]
