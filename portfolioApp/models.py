from django.db import models
from django.contrib.gis.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    home_address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    location = models.PointField()
