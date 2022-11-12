from django.test import TestCase
from rest_framework.test import APIClient

# Create your tests here.
client = APIClient()


class AuthTests(TestCase):

    def test_login(self):
        client.login(username='emre', password='emre')

    def test_logout(self):
        client.logout()
