from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import UserProfileForm
from .models import CustomUser, UserProfile
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import update_session_auth_hash
from .forms import CustomUserForm
from django.contrib.auth.forms import SetPasswordForm
from auditlog.models import LogEntry
from allauth.account.views import SignupView

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

            # Log the user login event
            log_entry = LogEntry.objects.log_create(
                instance=user,
                action='Login',
                user=request.user
            )

            return redirect('admin:index')  # Redirect to the admin index page

    return render(request, 'login.html')


class CustomSignupView(SignupView):
    template_name = 'signup.html'
    success_url = 'login'  

    def form_valid(self, form):
        response = super().form_valid(form)
        profile = form.instance.userprofile
        profile.name = form.cleaned_data['name']
        profile.save()
        return response



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
    user = request.user
    if request.method == 'POST':
        form = CustomUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CustomUserForm(instance=user)
    
    context = {
        'form': form
    }
    return render(request, 'edit_profile.html', context)

def map_view(request):
    users = CustomUser.objects.exclude(location=None)
    user_locations = [
        {
            'name': user.username,
            'lat': user.location.y,
            'lng': user.location.x
        }
        for user in users
    ]
    context = {'user_locations': user_locations}
    return render(request, 'map.html', context)


