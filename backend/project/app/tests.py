from django.test import TestCase
from .models import Client, Order, Product

import datetime
# Create your tests here.
from unittest import skip

class myTest(TestCase):
    def test_one(self):
        product1 = Product(product_name="milk")
        product2 = Product(product_name="rice")
        product3 = Product(product_name="spagetti")
        product1.save()
        product2.save()
        product3.save()
        order1 = Order()
        order2 = Order()
        order3 = Order()
        order1.save()
        order2.save()
        order3.save()
        order1.product.add(product1,product2,product3)
        order2.product.add(product1,product3)
        order3.product.add(product1)

        print(order2.product.all())
        # print(product3.order_set.all())

        # print(Product.objects.all())
        self.assertEqual("a","a")


