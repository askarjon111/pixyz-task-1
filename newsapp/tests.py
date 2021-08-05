from django.test import TestCase
from django.contrib.auth.models import AnonymousUser
from django.test import TestCase, RequestFactory

from .views import *


class ListPostsTestCase(TestCase):
    longMessage = True
    def test_get(self):
        status_code = 200
        view_class = ListPosts
        
        req = RequestFactory().get('/')
        req.user = AnonymousUser()
        resp = ListPosts.as_view()(req, *[], **{})
        self.assertEqual(resp.status_code, 200)


class DetailPostTestCase(TestCase):
    longMessage = True
    def test_get(self):
        status_code = 200
        view_class = DetailPost.as_view()
        
        req = RequestFactory().get(obj.pk)
        req.user = AnonymousUser()
        resp = DetailPost.as_view()(req, *[], **{})
        self.assertEqual(resp.status_code, 200)
