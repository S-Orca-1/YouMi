from rest_framework import serializers
from .models import User, Session, PsychologistTime


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'full_name', 'gender', 'birthday', 'citizenship', 'country_city', 'image', 'phone', 'email',
                  'social_media', 'is_psychologist']

    id = serializers.IntegerField(read_only=True)


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ['id', 'user', 'psychologist', 'data']

    id = serializers.IntegerField(read_only=True)


class PsychologistTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PsychologistTime
        fields = ['id', 'day', 'start', 'end']

    id = serializers.IntegerField(read_only=True)
