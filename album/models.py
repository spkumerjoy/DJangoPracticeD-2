from django.db import models
from musician.models import Musician

RATING_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=150)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE, related_name="albums")
    release_date = models.DateField(auto_now_add=True)
    rating = models.IntegerField(choices=RATING_CHOICES)

    def __str__(self):
        return self.name