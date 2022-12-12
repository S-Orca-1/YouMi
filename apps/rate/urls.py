from django.urls import path
from .views import RateAPIView

urlpatterns = [
    path('', RateAPIView.as_view()),
]
