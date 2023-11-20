from django.urls import path
from . import views
from .views import add_semester

urlpatterns = [
    path('add_semester/', views.add_semester, name='add_semester'),
]