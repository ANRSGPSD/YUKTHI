# yourapp/forms.py
from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['tenth_mark_card', 'twelfth_mark_card', 'aadhar_card', 'admission_order']
