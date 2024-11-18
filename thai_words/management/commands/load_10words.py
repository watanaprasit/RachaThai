import json
from django.core.management.base import BaseCommand
from thai_words.models import TenWords

class Command(BaseCommand):
    help = 'Load 10Words data from a JSON file into the database'

    def handle(self, *args, **kwargs):
        # Load the JSON file
        with open('thai_words/static/10words.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Loop through the JSON and create TenWords objects
        for item in data:
            TenWords.objects.create(
                word=item.get('word'),
                rtgs=item.get('rtgs'),
                meaning=item.get('meaning'),
                notes=item.get('notes', ''),
                index=item.get('index'),
                mp3=item.get('mp3', ''),
            )

        self.stdout.write(self.style.SUCCESS('Successfully loaded 10Words data into the database'))
