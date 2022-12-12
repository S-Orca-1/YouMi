from rest_framework import generics
from .serializers import RateSerializer
from .models import Rate


class RateAPIView(generics.ListAPIView):
    def get_queryset(self):
        return Rate.objects.all()

    def get_serializer_class(self):
        return RateSerializer
