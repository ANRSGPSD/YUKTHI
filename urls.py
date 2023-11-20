# yourappname/urls.py
from django.urls import path
from App import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    # Add other URLs as needed
]
