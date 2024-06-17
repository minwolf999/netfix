from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.hashers import make_password
from django.views.generic import CreateView, TemplateView

from .forms import CustomerSignUpForm, CompanySignUpForm, UserLoginForm
from .models import User, Company, Customer
from users import forms


def register(request):
    if request.user.username != "":
        return redirect('/')
    
    return render(request, 'users/register.html')


def CustomerSignUpView(request):
    if (request.method == 'POST'):
        form = CustomerSignUpForm(request.POST)
        if (form.is_valid()):
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            cryptedPassword = make_password(password)
            email = form.cleaned_data['email']

            user = User.objects.create(
                username = username,
                password = cryptedPassword,
                is_company = False,
                is_customer = True,
                email = email,
            )

            Customer.objects.create(
                user = user,
                birth = form.cleaned_data['birth'],
            )

            login(request, user)

            return redirect('/')
    
    form = CustomerSignUpForm()
    return render(request, 'users/register_company.html', context={'form':form})

def CompanySignUpView(request):
    if (request.method == 'POST'):
        form = CompanySignUpForm(request.POST)
        if (form.is_valid()):
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']

            user = User.objects.create_user(
                username = username,
                password = password,
                is_company = True,
                is_customer = False,
                email = email,
            )

            Company.objects.create(
                user = user,
                field = form.cleaned_data['field'],
                rating = form.cleaned_data['rating'],
            )

            login(request, user)
            return redirect('/')
    
    form = CompanySignUpForm()
    return render(request, 'users/register_company.html', context={'form':form})

def LoginUserView(request):
    if request.user.username != "":
        return redirect('/')
    
    form = forms.UserLoginForm()
    message = ''
    if (request.method == 'POST'):
        message = 'Identifiants invalides.'
        form = forms.UserLoginForm(request.POST)
        if (form.is_valid()):
            username = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(
                username = username,
                password = password,
            )

            if (user is not None):
                login(request, user)
                message = f'Bonjour, {user.username}! Vous êtes connecté'
                return redirect('/')
    
    return render(
    request, 'users/login.html', context={'form': form, 'message': message})

