

# Create your views here.
from django.shortcuts import render,redirect,reverse
from .forms import SemesterForm

def add_semester(request):
    if request.method == 'POST':
        form = SemesterForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return render(request,'success.html') # Redirect to a success page
    else:
        form = SemesterForm()

    return render(request, 'add_semester.html', {'form': form})
