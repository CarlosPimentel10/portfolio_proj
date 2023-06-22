from django import forms
from django.contrib.auth.forms import UserCreationForm
from portfolio_app.models import CustomUser, UserProfile



""" class UserProfileForm(UserCreationForm):
    name = forms.CharField()

    class Meta:
        model = CustomUser
        fields = ['name', 'username', 'password1', 'password2']
 """
class UserProfileForm(UserCreationForm):
    name = forms.CharField()

    class Meta:
        model = CustomUser
        fields = ['name', 'username', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        name = self.cleaned_data['name']
        if commit:
            user.save()
            user_profile = UserProfile(user=user, name=name)
            user_profile.save()
        return user

""" class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'home_address']
 """

class CustomUserForm(forms.ModelForm):
    password1 = forms.CharField(label='New Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm New Password', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'home_address']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")

        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data['password1']
        if password:
            user.set_password(password)
        if commit:
            user.save()
        return user