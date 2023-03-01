from django.db import models

# Create your models here.
class Finch(models.Model):
    species = models.CharField(max_length=100)
    beakLength = models.IntegerField()
    color = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.species} ({self.id})'