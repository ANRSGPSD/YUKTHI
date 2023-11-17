# views.py

from django.shortcuts import render, redirect
from .forms import UserDetailsForm
from .models import stu_personal_det,admin_stu_personal_det

# Create your views here.
def add_user_details(request):
    if request.method == 'POST':
        form = UserDetailsForm(request.POST)
        if form.is_valid():
            # Save data to Table1
            stu_personal_det_object = stu_personal_det.objects.create(
                Name=form.cleaned_data['Name'],
                FatherName=form.cleaned_data['FatherName'],
                MotherName=form.cleaned_data['MotherName'],
                Dob=form.cleaned_data['Dob'],
                Address=form.cleaned_data['Address'],
                BldGrp=form.cleaned_data['BldGrp'],
                Email=form.cleaned_data['Email'],
                PhoneNo=form.cleaned_data['PhoneNo'],
            )

            # Save data to Table2
            admin_stu_personal_det_object = admin_stu_personal_det.objects.create(
                Name=form.cleaned_data['Name'],
                FatherName=form.cleaned_data['FatherName'],
                MotherName=form.cleaned_data['MotherName'],
                Dob=form.cleaned_data['Dob'],
                Address=form.cleaned_data['Address'],
                BldGrp=form.cleaned_data['BldGrp'],
                Email=form.cleaned_data['Email'],
                PhoneNo=form.cleaned_data['PhoneNo'],
                
            )

            return redirect('add_user_details')  # Redirect to a success page
    else:
        form = UserDetailsForm()

    return render(request, 'add_user_details.html', {'form': form})
