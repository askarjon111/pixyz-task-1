from django.test import TestCase
from django.contrib.auth.models import AnonymousUser
from django.test import TestCase, RequestFactory
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


from .views import *


class ListPostsTestCase(TestCase):
    def create_post(self, title="title", body="body"):
        user = User.objects.create(username='testuser', is_superuser=True)
        return Post.objects.create(title=title, body=body, created_at=timezone.now(), author=user)

    def test_post_creation(self):
        post = self.create_post()
        self.assertTrue(isinstance(post, Post))
        self.assertEqual(post.__str__(), post.title)

    def post_list_view(self):
        post = self.create_post()
        url = reverse("newsapp.views.ListPosts")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertIn(post.title, resp.content)
