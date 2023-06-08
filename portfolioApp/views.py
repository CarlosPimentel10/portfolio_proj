from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
# Create your views here.


@login_required
def profile(request):
    # Retrieve the current user's profile
    profile = request.user.userprofile

    context = {
        'profile': profile
    }
    return render(request, 'portfolioApp/profile.html', context)

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
    return render(request, 'portfolioApp/edit_profile.html', context)
