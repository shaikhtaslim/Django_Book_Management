from django.db import models
# Create your models here.


class Book(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    published_date = models.DateField()

