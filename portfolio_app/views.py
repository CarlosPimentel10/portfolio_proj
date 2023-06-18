from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import UserProfileForm
from .models import CustomUser

# Create your views here.
def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def profile(request):
    # Retrieve the current user's profile
    profile = request.user.userprofile

    context = {
        'profile': profile
    }
    return render(request, 'profile.html', context)

@login_required
def edit_profile(request):
    # Retrieve the current user's profile
    profile = request.user.userprofile

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=profile)

    context = {
        'form': form
    }
    return render(request, 'edit_profile.html', context)

def map_view(request):
    # Retrieve all registered users' locations
    users = CustomUser.objects.exclude(location=None)

    context = {
        'users': users
    }
    return render(request, 'map.html', context)
