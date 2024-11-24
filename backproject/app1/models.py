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
    characters = models.ManyToManyField('Characters583', related_name='books1')
    povCharacters = models.ManyToManyField('Characters583', related_name='pov_books1')


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
    books = models.ManyToManyField(Books1, related_name='characters583', blank=True)
    pov_books = models.ManyToManyField(Books1, related_name='pov_characters583', blank=True)
    tvSeries = models.CharField(max_length=500)
    playedBy = models.CharField(max_length=500)
