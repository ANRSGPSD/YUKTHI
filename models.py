

# Create your models here.
from django.db import models

class Semester(models.Model):
    usn=models.CharField(max_length=10)
    semester_number = models.CharField(max_length=50)
    marks_obtained = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    total_marks = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    # Other fields if any...

    def str(self):
        return f"Semester {self.semester_number}"