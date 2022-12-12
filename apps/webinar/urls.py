from django.urls import path
from .views import WebinarAPIView, WebinarRetrieve, RegisterWebinarAPIView, PaymentAPIView

urlpatterns = [
    path('', WebinarAPIView.as_view()),
    path('<int:pk>/', WebinarRetrieve.as_view()),
    path('register-webinar/', RegisterWebinarAPIView.as_view()),
    path('payment/', PaymentAPIView.as_view()),
]
