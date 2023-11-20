# yourappname/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Add any additional fields you want
    # Example: profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    pass
