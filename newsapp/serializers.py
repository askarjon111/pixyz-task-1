from rest_framework import serializers
from .models import *


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'body', 'category', 'author']
        extra_kwargs = {'author': {'read_only': True}}

    # def create(self, validated_data):
    #     authenticated_user = self.context['request'].user
    #     post = Post.objects.create(**validated_data, user=authenticated_user)
    #     return post


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
