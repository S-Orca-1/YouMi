from rest_framework import generics
from .serializers import UserSerializer, SessionSerializer, PsychologistTimeSerializer
from .models import User, Session, PsychologistTime


class UserAPIView(generics.ListCreateAPIView):
    def get_queryset(self):
        return User.objects.all()

    def get_serializer_class(self):
        return UserSerializer


class SessionAPIView(generics.ListCreateAPIView):
    def get_queryset(self):
        return Session.objects.all()

    def get_serializer_class(self):
        return SessionSerializer


class PsychologistAPIView(generics.ListAPIView):
    def get_queryset(self):
        return User.objects.filter(is_psychologist=True).all()

    def get_serializer_class(self):
        return UserSerializer


class PsychologistTimeAPIView(generics.ListCreateAPIView):
    def get_queryset(self):
        return PsychologistTime.objects.all()

    def get_serializer_class(self):
        return PsychologistTimeSerializer
