from django.shortcuts import render
from .models import ThaiConsonant, ThaiVowel

# Create your views here.
def home(request):
    consonants = ThaiConsonant.objects.all().order_by('ranking')
    return render(request, 'home.html', {'consonants': consonants})

def vowels(request):
    vowels = ThaiVowel.objects.all().order_by('long_ranking')
    return render(request, 'vowels.html', {'vowels': vowels})