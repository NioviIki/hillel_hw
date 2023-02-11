from django.db import models

class City(models.Model):
    city = models.CharField(max_length=30)

    def __str__(self):
        return self.city

class Product(models.Model):
    product = models.CharField(max_length=50)

    def __str__(self):
        return self.product


class Vendor(models.Model):
    company = models.CharField(max_length=30)
    vendor = models.OneToOneField(City, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.company} to {self.vendor}'
class Client(models.Model):
    product = models.ManyToManyField(Product)
    key = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return f'Client {self.key_id} from {self.key} buy {list(self.product.all())}'

