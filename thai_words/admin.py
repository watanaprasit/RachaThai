from django.contrib import admin
from .models import ThaiConsonant, ThaiVowel

# Define the custom admin interface
class ThaiConsonantAdmin(admin.ModelAdmin):
    list_display = ['ranking', 'letter', 'thai_word', 'rtgs', 'meaning', 'emoji']
    search_fields = ['letter', 'thai_word', 'meaning']
    
class ThaiVowelAdmin(admin.ModelAdmin):
    list_display = ['long_ranking', 'letter', 'thai_word', 'rtgs', 'ipa', 'pronunciation']
    search_fields = ['letter', 'thai_word', 'rtgs', 'ipa']

# Register the model and its custom admin
admin.site.register(ThaiConsonant, ThaiConsonantAdmin)
admin.site.register(ThaiVowel, ThaiVowelAdmin)


