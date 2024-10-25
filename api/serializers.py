from rest_framework import serializers
from blogs.models import Blogs
from accounts.models import Accounts

class BolgsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogs
        fields = ['title', 'published_on']


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = ["email", "username", "password"]