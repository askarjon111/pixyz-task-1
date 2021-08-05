from django.urls import path
from .views import *

urlpatterns = [
    path('', ListPosts.as_view(), name="index"),
    path('topposts/', ListTopPosts.as_view(), name="topposts"),
    path('mostviewed/', MostViewedPosts.as_view(), name="mostviewed"),
    path('posts/<int:pk>', DetailPost.as_view(), name="postdetail")
]
