from django.core.management.base import BaseCommand
from django.core.files import File
from thai_words.models import TenWords
import os

class Command(BaseCommand):
    help = 'Load MP3 files into TenWords model based on index'

    def handle(self, *args, **kwargs):
        # Directory containing MP3 files
        mp3_directory = 'thai_words/media/!10wordsSound'

        # Loop through the TenWords model
        for word in TenWords.objects.all():
            try:
                # Ensure we are matching by index in your TenWords model
                index = word.index
                file_name = f"{index}.mp3"  # MP3 filename using the index

                # Build the full file path
                file_path = os.path.join(mp3_directory, file_name)

                # Check if the file exists
                if os.path.exists(file_path):
                    with open(file_path, 'rb') as mp3_file:
                        word.mp3.save(file_name, File(mp3_file))  # Save the MP3 file to the model field

                    word.save()  # Save the model with the updated MP3 file
                    self.stdout.write(self.style.SUCCESS(f"MP3 for index {index} added."))
                else:
                    self.stdout.write(self.style.WARNING(f"MP3 file {file_name} not found at {file_path}."))
                    
            except TenWords.DoesNotExist:
                self.stdout.write(self.style.WARNING(f"TenWords with index {index} does not exist."))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"An error occurred: {str(e)}"))

