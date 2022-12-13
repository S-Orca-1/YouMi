from rest_framework import serializers
from .models import Webinar, Registration, Payment


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


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'card_number', 'validity_period', 'cvv', 'card_holder']

    id = serializers.IntegerField(read_only=True)
