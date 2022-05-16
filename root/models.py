from operator import mod
from django.db import models

# Create your models here.

class Url(models.Model):
    full_url = models.CharField(unique=True ,max_length=400)
    short_url = models.CharField(unique=True, max_length=20)

    def __str__(self):
        return self.full_url
