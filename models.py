from django.db import models

# Create your models here.

#table for personal details stored for users
class stu_personal_det(models.Model):
    Name=models.CharField(max_length=300)
    FatherName=models.CharField(max_length=300)
    MotherName=models.CharField(max_length=300)
    Dob=models.DateField()
    Address=models.CharField(max_length=500)
    BldGrp=models.CharField(max_length=3)
    Email=models.EmailField(max_length=100)
    PhoneNo=models.CharField(max_length=10)

# table for personal details stored for admin

class admin_stu_personal_det(models.Model):
    Name=models.CharField(max_length=300)
    FatherName=models.CharField(max_length=300)
    MotherName=models.CharField(max_length=300)
    Dob=models.DateField()
    Address=models.CharField(max_length=500)
    BldGrp=models.CharField(max_length=3)
    Email=models.EmailField(max_length=100)
    PhoneNo=models.CharField(max_length=10)