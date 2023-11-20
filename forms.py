from django import forms
from .models import Semester

class SemesterForm(forms.ModelForm):
    class Meta:
        model = Semester
        fields = ['usn','semester_number', 'marks_obtained', 'total_marks']

    SEMESTER_CHOICES = [
        ('1', 'Semester 1'),
        ('2', 'Semester 2'),
        ('3', 'Semester 3'),
        ('4', 'Semester 4'),
        ('5', 'Semester 5')
        # Add more as needed...
    ]
    usn=forms.CharField(max_length=10)
    semester_number = forms.ChoiceField(choices=SEMESTER_CHOICES)
    marks_obtained = forms.DecimalField(max_digits=5, decimal_places=2)
    total_marks = forms.DecimalField(max_digits=5, decimal_places=2)