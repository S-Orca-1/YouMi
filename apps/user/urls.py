from django.urls import path
from .views import UserAPIView, SessionAPIView, PsychologistAPIView

urlpatterns = [
    path('', UserAPIView.as_view()),
    path('session/', SessionAPIView.as_view()),
    path('psychologist/', PsychologistAPIView.as_view()),
]
