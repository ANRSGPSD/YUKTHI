from django.urls import path, include
from . import views


urlpatterns = [
   
    path('firstpage', views.firstPage,name='root'),
    path('secondpage',views.secondpage,name='secondpage'),
    path('App1',views.App1,name='App1'),
    path('App1/details/<int:id>',views.details,name='details'),
    path('form/', views.student_form, name='App1_student'),
    
    path('success/', views.success, name='success'),
    path('search_student/', views.search_student, name='search_student'),
    path('update-student/<int:student_id>/', views.update_student, name='update_student'),
]  