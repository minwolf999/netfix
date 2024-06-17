from django.urls import path
from django.contrib.auth import views

from .forms import UserLoginForm
from . import views as v

urlpatterns = [
    path('', v.register, name='register'),
    
    path('customer/', v.CustomerSignUpView, name='register_customer'),
    path('company/', v.CompanySignUpView, name='register_company'),
    path('login/', v.LoginUserView, name='login_user')
]
