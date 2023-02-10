from django.db import models

class City(models.Model):
    city = models.CharField(max_length=30)

class Product(models.Model):
    product = models.CharField(max_length=50)

class Vendor(models.Model):
    company = models.CharField(max_length=30)
    vendor = models.OneToOneField(City, on_delete=models.CASCADE)

class Client(models.Model):
    product = models.ManyToManyField(Product)
    key = models.ForeignKey(City, on_delete=models.CASCADE)

