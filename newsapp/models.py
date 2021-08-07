from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Category(models.Model):
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField(blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, blank=True, null=True, related_name="posts")
    image = models.ImageField(upload_to="posts/%Y/%m/%d", blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    featured = models.BooleanField(default=False)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class PostViewed(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.post.title
