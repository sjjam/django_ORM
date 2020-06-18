from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=150)
    title_en = models.CharField(max_length=150)
    audience = models.IntegerField(null=True)
    open_date = models.DateField()
    genre = models.CharField(max_length=150)
    watch_grade = models.CharField(max_length=150)
    score = models.FloatField(null=True)
    poster_url = models.TextField(null=True)
    description = models.TextField(null=True)