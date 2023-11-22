# yourappname/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserRegistrationForm, UserLoginForm

def user_page(request):
    return render(request, 'user_page.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Authenticate the user
            authenticated_user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],  # Ensure you have a password field in your form
            )

            # Log in the user if authentication is successful
            if authenticated_user:
                login(request, authenticated_user)
                return redirect('user_page')  # Redirect to your home page

    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user:
                login(request, user)
                return redirect('user_page')  # Redirect to your home page

    else:
        form = UserLoginForm()

    return render(request, 'user_login.html', {'form': form})
