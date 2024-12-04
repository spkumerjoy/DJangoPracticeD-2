from django.db import models

INSTRUMENT_CHOICES = [
        ('guitar', 'Guitar'),
        ('drums', 'Drums'),
        ('bass', 'Bass'),
        ('piano', 'Piano'),
        ('violin', 'Violin'),
        ('vocals', 'Vocals'),
    ]
# Create your models here.
class Musician(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    instrument_type = models.CharField(max_length=50, choices=INSTRUMENT_CHOICES)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"