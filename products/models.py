from django.db import models

# Product model
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)


# Offer model
class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=500)
    discount = models.FloatField()
