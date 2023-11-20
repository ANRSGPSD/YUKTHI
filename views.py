# yourapp/views.py
from django.shortcuts import render, redirect,get_object_or_404
from .forms import StudentForm
from .models import Student
from django.http import HttpResponse


def upload_student_files(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_student_files')
    else:
        form = StudentForm()

    files = Student.objects.all()
    return render(request, 'upload_student_files.html', {'form': form, 'files': files})
# yourapp/views.py (Continued)

