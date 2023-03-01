from django.db import models

# Create your models here.
class Finch(models.Model):
    species = models.CharField(max_length=100),
    beakLength = models.IntegerField(),
    bodyWeight = models.IntegerField(),
    color = models.CharField(max_length=100),
    habitat = models.CharField(max_length=100)

    