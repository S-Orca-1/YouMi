from rest_framework import serializers
from .models import Blog, Category, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']
    id = serializers.IntegerField(read_only=True)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

    id = serializers.IntegerField(read_only=True)


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'category', 'tags', 'image', 'content', 'created_at']

    created_at = serializers.DateTimeField(read_only=True)
    id = serializers.IntegerField(read_only=True)
