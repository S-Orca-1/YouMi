from rest_framework import generics
from .serializers import EducationSerializer, SpecialtySerializer, ProfessionalDataSerializer, \
    AdditionalQuestionSerializer
from .models import Education, Specialty, ProfessionalData, AdditionalQuestion


class EducationAPIView(generics.CreateAPIView):
    def get_queryset(self):
        return Education.objects.all()

    def get_serializer_class(self):
        return EducationSerializer


class SpecialtyAPIView(generics.ListCreateAPIView):
    def get_serializer_class(self):
        return SpecialtySerializer

    def get_queryset(self):
        return Specialty.objects.all()


class ProfessionalDataAPIView(generics.ListCreateAPIView):
    def get_serializer_class(self):
        return ProfessionalDataSerializer

    def get_queryset(self):
        return ProfessionalData.objects.all()


class AdditionalQuestionAPIView(generics.ListCreateAPIView):
    def get_serializer_class(self):
        return AdditionalQuestionSerializer

    def get_queryset(self):
        return AdditionalQuestion.objects.all()
