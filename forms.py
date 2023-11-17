# forms.py

from django import forms
from .models import stu_personal_det

class UserDetailsForm(forms.ModelForm):
    class Meta:
        model = stu_personal_det
        fields = '__all__'
        # Add more fields as needed
