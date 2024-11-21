from django.urls import path
from . import views  # Import your views

urlpatterns = [
    path('', views.home, name='home'),  # Map the root URL to the home view
    path('vowels', views.vowels, name='vowels'),  
    path('consonant-sounds', views.consonant_sounds, name='consonant-sounds'),
    path('consonant/<str:letter>/', views.each_consonant, name='each_consonant'),  
    path('ten-words/', views.ten_words, name='ten_words'),
    path('api/consonants/', views.consonant_list, name='consonant-list'),  # New API endpoint
]
