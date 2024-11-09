import json
from django.core.management.base import BaseCommand
from thai_words.models import ThaiConsonant  # Adjust 'your_app' to your actual app name

class Command(BaseCommand):
    help = 'Load Thai consonants data from a JSON file'

    def handle(self, *args, **kwargs):
        # Specify the path to your merged JSON file
        json_file_path = 'thai_words/static/merged.json'  # Change this to the actual path of your merged JSON file
        
        try:
            # Open and load the merged JSON data file
            with open(json_file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # Iterate over the JSON data and insert each record into the database
            for item in data:
                ThaiConsonant.objects.create(
                    ranking=item.get("Ranking"),
                    letter=item.get("Letter"),
                    thai_word=item.get("Thai Word"),
                    rtgs=item.get("RTGS"),
                    meaning=item.get("Meaning"),
                    emoji=item.get("Emoji", "")  # Default to empty string if emoji is not found
                )

            self.stdout.write(self.style.SUCCESS('Data loaded successfully'))

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'File not found: {json_file_path}'))
        except json.JSONDecodeError:
            self.stdout.write(self.style.ERROR('Error decoding the JSON file'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'An error occurred: {str(e)}'))
