import json
from django.core.management.base import BaseCommand
from thai_words.models import ThaiVowel

class Command(BaseCommand):
    help = 'Load Thai vowels data from a JSON file'

    def handle(self, *args, **kwargs):
        # Specify the correct path to your merged vowels long JSON file
        json_file_path = '/Users/darylwatanaprasit/Desktop/thai_app/thai_words/static/merged_vowels_long.json'
        
        try:
            # Open and load the merged JSON data file
            with open(json_file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # Iterate over the JSON data and insert each record into the database
            for item in data:
                ThaiVowel.objects.create(
                    long_ranking=item.get("long-ranking"),
                    letter=item.get("letter"),
                    thai_word=item.get("thai word"),
                    rtgs=item.get("rtgs"),
                    ipa=item.get("ipa"),
                    pronunciation=item.get("pronunciation")
                )

            self.stdout.write(self.style.SUCCESS('Data loaded successfully'))

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'File not found: {json_file_path}'))
        except json.JSONDecodeError:
            self.stdout.write(self.style.ERROR('Error decoding the JSON file'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'An error occurred: {str(e)}'))
