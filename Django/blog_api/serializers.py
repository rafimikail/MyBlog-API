from rest_framework import serializers
from blog.models import Post
from django.conf import settings


class PostSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%m/%d/%y %H:%M")

    class Meta:
        model = Post
        fields = ('category', 'id', 'title', 'slug', 'author',
                  'excerpt', 'content', 'status','created_at')


class UserRegisterSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ('email', 'user_name', 'first_name')
        extra_kwargs = {'password': {'write_only': True}}