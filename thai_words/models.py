from django.db import models

class ThaiConsonant(models.Model):
    ranking = models.IntegerField()
    letter = models.CharField(max_length=1) 
    thai_word = models.CharField(max_length=255)
    rtgs = models.CharField(max_length=255)
    meaning = models.CharField(max_length=255)
    emoji = models.CharField(max_length=5, blank=True, null=True) 
    audio_pronunciation = models.FileField(upload_to='', blank=True, null=True)
 
    def __str__(self):
        return f"{self.letter} - {self.meaning}"

    class Meta:
        ordering = ['ranking']  # Ensure the objects are ordered by ranking

class ThaiVowel(models.Model):
    long_ranking = models.IntegerField()
    letter = models.CharField(max_length=10)  # Adjusted for longer vowel characters
    thai_word = models.CharField(max_length=255)
    rtgs = models.CharField(max_length=255)
    ipa = models.CharField(max_length=50)
    pronunciation = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.letter} - {self.thai_word}"

    class Meta:
        ordering = ['long_ranking']  # Ensure the objects are ordered by ranking
        
class TenWords(models.Model):
    index = models.IntegerField(unique=True)  # Make index unique to avoid duplicates
    word = models.CharField(max_length=255)
    rtgs = models.CharField(max_length=255)
    meaning = models.CharField(max_length=255)
    notes = models.TextField(blank=True, null=True)
    mp3 = models.FileField(upload_to='ten_words_mp3/', blank=True, null=True)

    def __str__(self):
        return f"{self.index}. {self.word} - {self.meaning}"

    class Meta:
        ordering = ['index']  # Ensures the objects are ordered by index
