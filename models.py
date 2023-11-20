# yourapp/models.py
from django.db import models

class Student(models.Model):
    tenth_mark_card = models.FileField(upload_to='tenth_marks_card/')
    twelfth_mark_card = models.FileField(upload_to='twelfth_marks_card/')
    aadhar_card = models.FileField(upload_to='aadhar_card/')
    admission_order = models.FileField(upload_to='admission_order/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
