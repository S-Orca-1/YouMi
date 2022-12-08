from rest_framework import serializers
from .models import Webinar, Registration


class WebinarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Webinar
        fields = ['title', 'image', 'content', 'type', 'price', 'date']


class WebinarRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Webinar
        fields = ['id', 'title', 'type', 'image', 'video', 'tags', 'price', 'content', 'date']

    id = serializers.IntegerField(read_only=True)


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ['id', 'webinar', 'first_name', 'last_name', 'email']

    id = serializers.IntegerField(read_only=True)