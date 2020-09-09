from django.db import models

# Create your models here.

class City(models.Model):
    city = models.CharField("City Name", max_length=30)

    def __str__(self):
        return self.city