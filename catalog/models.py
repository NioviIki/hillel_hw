from django.db import models


class City(models.Model):
    city = models.CharField(max_length=30)

    def __str__(self):
        return self.city


class Product(models.Model):
    product = models.CharField(max_length=50)

    def __str__(self):
        return self.product


class Retailer(models.Model):
    company = models.CharField(max_length=30)
    city = models.OneToOneField(City, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.company} to {self.city}'


class Client(models.Model):
    product = models.ManyToManyField(Product)
    key = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return f'Client {self.key_id} from {self.key} buy {list(self.product.all())}'

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
