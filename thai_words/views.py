from django.shortcuts import render, get_object_or_404
from .models import ThaiConsonant, ThaiVowel, TenWords
from django.http import JsonResponse

# Create your views here.
def home(request):
    consonants = ThaiConsonant.objects.all().order_by('ranking')
    return render(request, 'home.html', {'consonants': consonants})

def vowels(request):
    vowels = ThaiVowel.objects.all().order_by('long_ranking')
    return render(request, 'vowels.html', {'vowels': vowels})

def consonant_sounds(request):
    consonants = ThaiConsonant.objects.all().order_by('ranking')
    return render(request, 'consonant-sounds.html', {'consonants': consonants})

def each_consonant(request, letter):
    consonant = get_object_or_404(ThaiConsonant, letter=letter)
    return render(request, 'each.html', {'consonant': consonant})

def ten_words(request):
    words = TenWords.objects.all().order_by('index')  
    return render(request, 'ten_words.html', {'words': words})

#Json Api for React Frontend
def consonant_list(request):
    consonants = ThaiConsonant.objects.all().order_by('ranking').values('letter', 'thai_word', 'rtgs', 'emoji')
    return JsonResponse(list(consonants), safe=False)
