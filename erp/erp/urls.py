from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('landing.urls')),
    path('accounting/', include('accounting.urls')),
    path('v1/test/api/', include('api.urls')),
]
