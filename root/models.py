from hashlib import md5
from operator import mod
from django.db import models

# Create your models here.

# Creating model for the url
class Url(models.Model):
    full_url = models.CharField(unique=True ,max_length=400)
    short_url = models.CharField(unique=True, max_length=20)

    def __str__(self):
        return self.full_url

# here we took the full url and we used hash to make the new short url and save it and we choose that the new short url will be from 5 charchater we
    @classmethod
    def create(self, full_url):
        temp_url = md5(full_url.encode()).hexdigest()[:5]
        try:
            obj = self.objects.create(full_url=full_url, short_url=temp_url)
        except:
            obj = self.objects.get(full_url=full_url)
        return obj
