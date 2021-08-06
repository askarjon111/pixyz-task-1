from django.test import TestCase, RequestFactory, Client
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from .views import *


client = Client()


class ListPostsTestCase(TestCase):
    def create_post(self, title="title", body="body"):
        user = User.objects.create(username='testuser', is_superuser=True)
        return Post.objects.create(title=title, body=body, created_at=timezone.now(), author=user)

    def test_post_creation(self):
        post = self.create_post()
        self.assertTrue(isinstance(post, Post))
        self.assertEqual(post.__str__(), post.title)

    def post_list_view_test(self):
        post = self.create_post()
        url = reverse("newsapp.views.ListPosts")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertIn(post.title, resp.content)

class DetailPostViewTest(TestCase):
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
