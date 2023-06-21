from django import forms
from django.contrib.auth.forms import UserCreationForm
from portfolio_app.models import CustomUser


class UserProfileForm(UserCreationForm):
    name = forms.CharField()

    class Meta:
        model = CustomUser
        fields = ['name', 'username', 'password1', 'password2']