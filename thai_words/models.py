from django.db import models

class ThaiConsonant(models.Model):
    ranking = models.IntegerField()
    letter = models.CharField(max_length=1)  # Assuming single character
    thai_word = models.CharField(max_length=255)
    rtgs = models.CharField(max_length=255)
    meaning = models.CharField(max_length=255)
    emoji = models.CharField(max_length=5, blank=True, null=True)  # Store emoji as text (max 5 chars for the emoji)

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
