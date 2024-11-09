from django.contrib import admin
from .models import ThaiConsonant  # Adjust if your app is named differently

# Define the custom admin interface
class ThaiConsonantAdmin(admin.ModelAdmin):
    list_display = ['ranking', 'letter', 'thai_word', 'rtgs', 'meaning', 'emoji']
    search_fields = ['letter', 'thai_word', 'meaning']

# Register the model and its custom admin
admin.site.register(ThaiConsonant, ThaiConsonantAdmin)

