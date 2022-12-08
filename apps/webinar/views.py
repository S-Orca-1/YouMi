from rest_framework import generics, status, response
from .serializers import WebinarRetrieveSerializer, RegistrationSerializer, WebinarSerializer
from .models import Webinar, Registration


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
