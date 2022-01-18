from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return 'Genre: {}'.format(self.name)

class Language(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return 'Language: {}'.format(self.name)

class Actor(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'

    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    )
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return 'Actor: {}'.format(self.name)

class Movie(models.Model):

    name = models.CharField(max_length=99)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    actor = models.ManyToManyField(Actor, related_name='movies')
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='movies')
    release_date = models.DateField(null=True, blank=True)
    overall_rating = models.FloatField()

    def __str__(self):
        return 'Movie: '.format(self.name)
