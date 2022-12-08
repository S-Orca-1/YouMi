from django.urls import path
from .views import WebinarAPIView

urlpatterns = [
    path('', WebinarAPIView.as_view())
]
