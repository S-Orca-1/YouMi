from django.urls import path
from .views import EducationAPIView, SpecialtyAPIView, ProfessionalDataAPIView, AdditionalQuestionAPIView


urlpatterns = [
    path('education/', EducationAPIView.as_view()),
    path('special/', SpecialtyAPIView.as_view()),
    path('pro_data/', ProfessionalDataAPIView.as_view()),
    path('add_ques/', AdditionalQuestionAPIView.as_view()),
]
