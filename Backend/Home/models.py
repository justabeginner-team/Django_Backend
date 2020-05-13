from django.db import models


# Create your models here.
class Destination(models.Model):
    price = models.IntegerField()
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='pics')
    description = models.TextField()
    offer = models.BooleanField(default=False)

#  this model works by adding destination points using django admin
