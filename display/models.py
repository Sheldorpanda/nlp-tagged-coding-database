from django.db import models

# Create your models here.


class Project(models.Model):
    link = models.CharField(max_length=200)
    Level = models.IntegerField(default=0)
    Language = models.IntegerField(default=0)
    Popularity = models.IntegerField(default=0)
    Legit = models.IntegerField(default=0)
