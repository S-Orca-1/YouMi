from django.urls import path, include

urlpatterns = [
    path('blog/', include('blog.urls')),
    path('webinar/', include('webinar.urls')),
    path('user/', include('user.urls')),
    path('rate/', include('rate.urls')),
    path('psychologist/', include('psychologist.urls')),
]
