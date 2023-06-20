from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from portfolio_app.models import UserProfile

User = get_user_model()

class Command(BaseCommand):
    help = 'Create UserProfile objects for existing CustomUser instances'

    def handle(self, *args, **options):
        users_without_profile = User.objects.filter(userprofile=None)

        for user in users_without_profile:
            UserProfile.objects.create(user=user)

        self.stdout.write(self.style.SUCCESS('User profiles created successfully.'))
