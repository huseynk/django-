from django.http import response
from django.test import TestCase
from .models import Articles
from django.contrib.auth import get_user_model
from django.urls import reverse

class ArticlesTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'testuser',
            email = 'testuser@gmail.com',
            password = 'password'
        )

        self.articles = Articles.objects.create(
            title = 'Yangi post',
            summary = 'Qisqa matn',
            photo = 'Rasm',
            date = 'Vaqt',
            text = 'Matn',
            author = self.user
        )
    
    def test_create(self):
        articles = Articles(title='Post mavzusi')
        self.assertEqual(str(articles), articles.title)

    def test_post_content(self):
        self.assertEqual(f'{self.articles.title}', 'Yangi post')
        self.assertEqual(f'{self.articles.summary}', 'Qisqa matn')
        self.assertEqual(f'{self.articles.photo}', 'Rasm')
        self.assertEqual(f'{self.articles.text}', 'Matn')
        self.assertEqual(f'{self.articles.author}', 'testuser')

    def test_list_page(self):
        response = self.client.get('article_list')
        self.assertNotEqual(response.status_code, 200)


    def test_detail_page(self):
        response = self.client.get('/<int:pk>/')
        no_response = self.client.get('/100000/')
        self.assertNotEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)

    def test_update_page(self):
        response = self.client.get('/<int:pk>/edit/')
        self.assertNotEqual(response.status_code, 200)
        no_response = self.client.get('/100000/edit/')
        self.assertEqual(no_response.status_code, 404)

    def test_delete_page(self):
        response = self.client.get('/<int:pk>/delete/')
        self.assertNotEqual(response.status_code, 200)
        no_response = self.client.get('/100000/delete/')
        self.assertEqual(no_response.status_code, 404)

    def test_new_page(self):
        response = self.client.get('/new/')
        self.assertNotEqual(response.status_code, 200)
