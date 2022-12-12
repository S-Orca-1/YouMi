from rest_framework import generics, status, response
from .serializers import WebinarRetrieveSerializer, RegistrationSerializer, WebinarSerializer, PaymentSerializer
from .models import Webinar, Registration, Payment


class WebinarAPIView(generics.ListAPIView):

    def get(self, request, *args, **kwargs):
        date = self.request.query_params.get('date')
        pre = Webinar.objects.filter(date__gte=date)
        arxiv = Webinar.objects.filter(date__lt=date)
        serializer1 = self.get_serializer(pre, many=True)
        serializer2 = self.get_serializer(arxiv, many=True)
        data = {
            'pre': serializer1.data,
            'arxiv': serializer2.data
        }
        return response.Response(data)

    def get_serializer_class(self):
        return WebinarSerializer


class WebinarRetrieve(generics.RetrieveAPIView):
    def get_queryset(self):
        return Webinar.objects.all()

    def get_serializer_class(self):
        return WebinarRetrieveSerializer


class RegisterWebinarAPIView(generics.CreateAPIView):
    def get_queryset(self):
        return Registration.objects.all()

    def get_serializer_class(self):
        return RegistrationSerializer


class PaymentAPIView(generics.CreateAPIView):
    def get_queryset(self):
        return Payment.objects.all()

    def get_serializer_class(self):
        return PaymentSerializer
