# Generated by Django 5.1.1 on 2024-12-01 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='releaseDate',
            new_name='release_date',
        ),
    ]