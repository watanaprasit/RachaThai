from django.contrib import admin
from .models import ThaiConsonant, ThaiVowel, TenWords

# Define the custom admin interface
class ThaiConsonantAdmin(admin.ModelAdmin):
    list_display = ['ranking', 'letter', 'thai_word', 'rtgs', 'meaning', 'emoji', 'audio_pronunciation']
    search_fields = ['letter', 'thai_word', 'meaning']
    
class ThaiVowelAdmin(admin.ModelAdmin):
    list_display = ['long_ranking', 'letter', 'thai_word', 'rtgs', 'ipa', 'pronunciation']
    search_fields = ['letter', 'thai_word', 'rtgs', 'ipa']
    
class TenWordsAdmin(admin.ModelAdmin):
    list_display = ['index', 'word', 'rtgs', 'meaning', 'notes', 'mp3']
    search_fields = ['word', 'rtgs', 'meaning']
    list_filter = ['index']  # Allow filtering by index for easier navigation

# Register the model and its custom admin
admin.site.register(ThaiConsonant, ThaiConsonantAdmin)
admin.site.register(ThaiVowel, ThaiVowelAdmin)
admin.site.register(TenWords, TenWordsAdmin)



