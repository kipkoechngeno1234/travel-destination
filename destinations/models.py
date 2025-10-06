from django.db import models

# Create your models here.
class Destination(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
    available = models.BooleanField(default=True)
