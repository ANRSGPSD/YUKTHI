# yourapp/urls.py
from django.urls import path
from .views import upload_student_files, view_uploaded_file

urlpatterns = [
    path('upload/', upload_student_files, name='upload_student_files'),
    
]
