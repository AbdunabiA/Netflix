from django.db import models

class Actor(models.Model):
    name = models.CharField(max_length=30)
    birth_date = models.DateField()
    gender = models.CharField(max_length=7)
    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=30)
    genre = models.CharField(max_length=15, choices=(("action", "action"), ("horror", "horror"), ("detective", "detevctive")))
    date = models.DateField()
    actors = models.ManyToManyField(Actor)
    def __str__(self):
        return self.title
