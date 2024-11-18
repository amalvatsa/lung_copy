from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin URL
    path('', include('detection.urls')),  # Include all URLs from the detection app
]
