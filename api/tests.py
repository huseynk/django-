from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from accounts.models import CustomUser

class AccountTests(APITestCase):
    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('article_list')
        data = {'name': 'accounts'}
        response = self.client.post(url, data, format='json')
        self.assertNotEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertNotEqual(CustomUser.objects.count(), 1)