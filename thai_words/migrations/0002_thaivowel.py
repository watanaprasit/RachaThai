# Generated by Django 5.1.3 on 2024-11-14 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thai_words', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThaiVowel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long_ranking', models.IntegerField()),
                ('letter', models.CharField(max_length=10)),
                ('thai_word', models.CharField(max_length=255)),
                ('rtgs', models.CharField(max_length=255)),
                ('ipa', models.CharField(max_length=50)),
                ('pronunciation', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['long_ranking'],
            },
        ),
    ]
