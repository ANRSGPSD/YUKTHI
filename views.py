# yourappname/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, LoginForm
def home(request):
    return render(request, 'home.html')
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to your home page
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to your home page
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
