from django.core.management.base import BaseCommand
from django.core.files import File
from thai_words.models import ThaiConsonant

class Command(BaseCommand):
    help = 'Load MP3 files into ThaiConsonant model'

    def handle(self, *args, **kwargs):
        for ranking in range(1, 45):  # Rankings 1 to 44
            try:
                consonant = ThaiConsonant.objects.get(ranking=ranking)
                file_path = f'thai_words/media/{ranking}.mp3'  # Correct path
                with open(file_path, 'rb') as mp3_file:
                    consonant.audio_pronunciation.save(f'{ranking}.mp3', File(mp3_file))
                consonant.save()
                self.stdout.write(self.style.SUCCESS(f"MP3 for ranking {ranking} added."))
            except ThaiConsonant.DoesNotExist:
                self.stdout.write(self.style.WARNING(f"ThaiConsonant with ranking {ranking} does not exist."))
