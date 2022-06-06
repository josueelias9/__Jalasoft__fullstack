import datetime
from django.db import models

# Create your models here.


class Client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name

class Product(models.Model):
    product_name = models.CharField(max_length=30)

    def __str__(self):
        return self.product_name

class Order(models.Model):
    products = models.JSONField(default={'default':'default'})
    date = models.DateField(default=datetime.date.today)
    publications = models.ManyToManyField(Product)


'''

+-------+          +-------+          +-------+
|       |1     many|       |many  many|       |
|client |----------| order |----------|product|
|       |          |       |          |       |
+-------+          +-------+          +-------+

'''