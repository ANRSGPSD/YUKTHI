# myapp/urls.py
from django.urls import path
from .views import register, user_login, user_page

urlpatterns = [
    path('register/', register, name='register'),
    path('user_login/', user_login, name='user_login'),
    path('user_page/', user_page, name='user_page'),
    
]
