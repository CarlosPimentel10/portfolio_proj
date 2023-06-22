from django.contrib import admin
from .models import CustomUser, UserProfile
# Register your models here.
from django.urls import reverse


admin.site.register(CustomUser)


