from django.db import models
from django.contrib.gis.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.gis.geos import Point
from auditlog.models import AuditlogHistoryField

class CustomUser(AbstractUser, models.Model):
    home_address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    location = models.PointField(default=Point(0, 0))
    history = AuditlogHistoryField()
    
    def __str__(self):
        return self.username

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.user.username
    



