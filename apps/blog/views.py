from rest_framework import generics, status, response
from .serializers import BlogSerializer, CategorySerializer, TagSerializer
from .models import Blog, Category, Tag


class CategoryAPIView(generics.ListCreateAPIView):
    def get_queryset(self):
        return Category.objects.all()

    def get_serializer_class(self):
        return CategorySerializer

