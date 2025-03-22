from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
   
    full_name = models.CharField(max_length=100)

    
    country = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    upazila = models.CharField(max_length=100)

    def __str__(self):
        return self.username