from rest_framework import serializers
from .models import Education, Specialty, ProfessionalData, AdditionalQuestion


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ['id', 'user', 'university', 'faculty', 'specialty', 'degree', 'start', 'finish', 'diplom']

    id = serializers.IntegerField(read_only=True)


class SpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = ['id', 'user', 'job_type', 'academy', 'course', 'training_hours', 'start', 'finish', 'certificate']

    id = serializers.IntegerField(read_only=True)


class ProfessionalDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessionalData
        fields = ['id', 'user', 'experience_company', 'experience_online', 'full_experience', 'client', 'time',
                  'therapy', 'therapy_hours', 'therapy_approach', 'chat', 'chat_hours', 'supervisor']

    id = serializers.IntegerField(read_only=True)


class AdditionalQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalQuestion
        fields = ['id', 'user', 'type', 'salary', 'other_job', 'job_time', 'about_me']

    id = serializers.IntegerField(read_only=True)
