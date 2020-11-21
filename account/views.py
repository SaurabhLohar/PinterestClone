from django.shortcuts import render, redirect
from .forms import UserRegisterForm,UserChange
from django.contrib.auth.forms import AuthenticationForm,UserChangeForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib import messages
from django.urls import reverse_lazy

from django.contrib.auth.views import PasswordChangeView

# Create your views here.

def register(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
            user = form.cleaned_data.get('username')
            # messages.success(request,f'Account Created')
    context = {
        'form': form
    }
    return render(request, 'account/register.html', context)

def userInfo(request):
    user = request.user
    form = UserChange(instance=user)
    if request.method == 'POST':
        form = UserChange(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    context = {
        'form': form
    }
    return render(request, 'account/changeInfo.html', context)


def userlogin(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'account/login.html', context)

def userLogout(request):
    logout(request)
    messages.info(request, f"You are now logged out")
    return redirect('home')


