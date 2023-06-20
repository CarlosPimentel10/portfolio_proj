from django.test import TestCase
from django.urls import reverse
# Create your tests here.

class HomePageTest(TestCase):
    
    def test_homepage_returns_200(self):
        url = reverse('home')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
