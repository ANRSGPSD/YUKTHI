# urls.py

from django.urls import path
from .views import add_user_details

urlpatterns = [
    path('add_user/', add_user_details, name='add_user_details'),
    # Add more URL patterns as needed
]
