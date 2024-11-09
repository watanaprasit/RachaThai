from django.urls import path
from . import views  # Import your views

urlpatterns = [
    path('', views.home, name='home'),  # Map the root URL to the home view
]
