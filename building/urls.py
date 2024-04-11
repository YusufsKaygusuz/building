from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('construction.urls')),
    path('secure-admin/', admin.site.urls),
]
