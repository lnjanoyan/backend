# do not forget to check data types and update them
from django.db import models


class Books1(models.Model):
    url = models.URLField(max_length=500)
    name = models.CharField(max_length=500)
    isbn = models.CharField(max_length=500)
    authors = models.CharField(max_length=500)
    numberOfPages = models.IntegerField()
    publisher = models.CharField(max_length=500)
    country = models.CharField(max_length=500)
    mediaType = models.CharField(max_length=500)
    released = models.CharField(max_length=500)
    characters = models.CharField(max_length=500)
    povCharacters = models.CharField(max_length=500)


class Characters583(models.Model):
    url = models.URLField()
    name = models.CharField(max_length=500)
    gender = models.CharField(max_length=500)
    culture = models.CharField(max_length=500)
    born = models.CharField(max_length=500)
    died = models.CharField(max_length=500)
    titles = models.CharField(max_length=500)
    aliases = models.CharField(max_length=500)
    father = models.CharField(max_length=500)
    mother = models.CharField(max_length=500)
    spouse = models.CharField(max_length=500)
    allegiances = models.CharField(max_length=500)
    books = models.ForeignKey(Books1, related_name='chars', on_delete=models.CASCADE)
    povBooks = models.CharField(max_length=500)
    tvSeries = models.CharField(max_length=500)
    playedBy = models.CharField(max_length=500)
