# myapp/models.py
from django.db import models

class UserProfile(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=100)  # Use a more secure method in a real project
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username
