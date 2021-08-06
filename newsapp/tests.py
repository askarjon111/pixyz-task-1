import json
from django.test import TestCase, Client
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from .views import *


client = Client()


class GETNewsTest(TestCase):
    def setUp(self):
        user = User.objects.create(username='testuser', is_superuser=True)

        self.post1 = Post.objects.create(
            title='Post 1', body='Test Post 1 body', author=user)
        self.post2 = Post.objects.create(
            title='Post 2', body='Test Post 2 body', author=user)
        self.post3 = Post.objects.create(
            title='Post 3', body='Test Post 3 body', author=user)
        self.post3 = Post.objects.create(
            title='Post 4', body='Test Post 4 body', author=user)

    def test_get_all_posts(self):
        response = client.get(reverse('index'))
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_valid_single_post(self):
        response = client.get(
            reverse('postdetail', kwargs={'pk': self.post1.pk}))
        post = Post.objects.get(pk=self.post1.pk)
        serializer = PostSerializer(post)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_post(self):
        response = client.get(
            reverse('postdetail', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
   

class POSTNewsTest(TestCase):
    def setUp(self):
        user = User.objects.create(username='testuser', is_superuser=True)
        self.valid_post = {
            'title': 'Post1',
            'body': 'Test',
            'author': 1,
        }
        self.invalid_post = {
            'title': '',
            'body': 'Test',
            'author': 1,
        }
        

    def test_create_valid_post(self):
        response = client.post(
            reverse('index'),
            data=json.dumps(self.valid_post),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_post(self):
        response = client.post(
            reverse('index'),
            data=json.dumps(self.invalid_post),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class PUTDeleteNewsTest(TestCase):
    def setUp(self):
        user = User.objects.create(username='testuser', is_superuser=True)
        self.post1 = Post.objects.create(
            title='Post 1', body='Test Post 1 body', author=user)
        self.post2 = Post.objects.create(
            title='Post 2', body='Test Post 2 body', author=user)

        self.valid_post = {
            'title': 'Post2',
            'body': 'Test',
            'author': 1,
        }
        self.invalid_post = {
            'title': '',
            'body': 'Test',
            'author': 1,
        }

    # Update test

    def test_valid_update_post(self):
        response = client.put(
            reverse('postdetail', kwargs={'pk': self.post1.pk}),
            data=json.dumps(self.valid_post),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_post(self):
        response = client.put(
            reverse('postdetail', kwargs={'pk': self.post2.pk}),
            data=json.dumps(self.invalid_post),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    
    # Delete test

    def test_valid_delete_post(self):
        response = client.delete(
            reverse('postdetail', kwargs={'pk': self.post1.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_post(self):
        response = client.delete(
            reverse('postdetail', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)