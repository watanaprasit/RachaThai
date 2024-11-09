from django.shortcuts import render
from .models import ThaiConsonant

# Create your views here.
def home(request):
    consonants = ThaiConsonant.objects.all().order_by('ranking')
    return render(request, 'home.html', {'consonants': consonants})