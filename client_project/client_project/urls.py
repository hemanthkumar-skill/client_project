from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),         # Main interface
    path('api/', include('core.api_urls')),  # API endpoints
]
