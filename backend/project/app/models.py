import datetime
from django.db import models

# Create your models here.


class Client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name

class Product(models.Model):
    product_name = models.CharField(max_length=30,default='')
    api_key = models.CharField(max_length=30, default='')

    def __str__(self):
        return self.api_key

class Order(models.Model):
    # client = models.ForeignKey(Client,default=1, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    product = models.ManyToManyField(Product)


'''

+-------+          +-------+          +-------+
|       |1     many|       |many  many|       |
|client |----------| order |----------|product|
|       |          |       |          |       |
+-------+          +-------+          +-------+

'''