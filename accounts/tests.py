from django.urls import reverse
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import CustomUser

class LoginTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'huseyn',
            'password': 'secret'
        }
        CustomUser.objects.create_user(**self.credentials)

    def test_login(self):
        response = self.client.post('/login/')
        self.assertNotEqual(response.status_code, 200)
    

class SignUpPageTests(TestCase):
    def setUp(self) -> None:
        self.username = 'testuser'
        self.email = 'testuser@gmail.com'
        self.first_name = 'first_name'
        self.last_name = 'last_name'
        self.age = 20
        self.password = 'password'

    def test_signup_page_url(self):
        response = self.client.get("/signup/")
        self.assertNotEqual(response.status_code, 200)
        # self.assertTemplateUsed(response, template_name='registration/signup.html')

    def test_signup_page_view_name(self) -> None:
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='registration/signup.html')

    def test_signup_form(self):
        response = self.client.post(reverse('signup'), data={
            'username': self.username,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age,
            'password1': self.password,
            'password2': self.password
        })
        self.assertEqual(response.status_code, 200)

        users = get_user_model().objects.all()
        self.assertNotEqual(users.count(), 1)



# Create your tests here.
