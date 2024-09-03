from django.contrib import admin
from django.urls import path
from .views import LoginAPI  # Make sure this import is correct

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginAPI.as_view(), name='login'),
]
