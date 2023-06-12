from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from django.shortcuts import render
from .models import CustomUser
# Create your views here.


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
            return redirect('profile.html')
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

