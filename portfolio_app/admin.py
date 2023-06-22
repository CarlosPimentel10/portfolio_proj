from django.contrib import admin
from .models import CustomUser, UserProfile
# Register your models here.
from django.urls import reverse
from django.utils.html import format_html
from .models import UserProfile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

admin.site.register(CustomUser)


