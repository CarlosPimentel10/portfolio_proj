from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model


User = get_user_model()


class HomeViewTest(TestCase):
    def test_home_view(self):
        client = Client()
        response = client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')


class LoginViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_login_view_with_valid_credentials(self):
        client = Client()
        response = client.post(reverse('login'), {'username': 'testuser', 'password': 'testpassword'})
        self.assertRedirects(response, reverse('admin:index'))

    def test_login_view_with_invalid_credentials(self):
        client = Client()
        response = client.post(reverse('login'), {'username': 'invaliduser', 'password': 'invalidpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')


class SignupViewTest(TestCase):
    def test_signup_view_with_valid_data(self):
        client = Client()
        response = client.post(reverse('signup'), {
            'name': 'Test User',
            'username': 'testuser',
            'password1': 'testpassword',
            'password2': 'testpassword'
        })
        self.assertRedirects(response, reverse('login'))

        user = User.objects.get(username='testuser')
        self.assertIsNotNone(user)
        self.assertEqual(user.userprofile.name, 'Test User')

    def test_signup_view_with_invalid_data(self):
        client = Client()
        response = client.post(reverse('signup'), {
            'name': 'Test User',
            'username': 'testuser',
            'password1': 'testpassword',
            'password2': 'differentpassword'  # Invalid password confirmation
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')
        self.assertFormError(response, 'form', 'password2', 'The two password fields didn’t match.')


class ProfileViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = Client()
        self.client.login(username='testuser', password='testpassword')

    def test_profile_view(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')
        self.assertEqual(response.context['profile'], self.user.userprofile)


class EditProfileViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = Client()
        self.client.login(username='testuser', password='testpassword')

    def test_edit_profile_view_with_valid_data(self):
        response = self.client.post(reverse('edit_profile'), {'username': 'newusername'})
        self.assertRedirects(response, reverse('profile'))
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, 'newusername')

    def test_edit_profile_view_with_invalid_data(self):
        response = self.client.post(reverse('edit_profile'), {'username': ''})  # Empty username
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_profile.html')
        self.assertFormError(response, 'form', 'username', 'This field is required.')


class MapViewTest(TestCase):
    def test_map_view(self):
        client = Client()
        response = client.get(reverse('map_view'))
       
