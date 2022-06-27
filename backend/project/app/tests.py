from django.test import TestCase
from .models import Client, Order, Product

import datetime
# Create your tests here.
from unittest import skipIf

class myTest(TestCase):
    @skipIf(True, "I don't want to run this test yet")
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

    @skipIf(True, "Test if date atribute of Order model is working properlly")
    def test_two(self):
        myDate = datetime.date(2022,1,1)
        order = Order(date=myDate)
        self.assertEqual(myDate,order.date)


    @skipIf(False, "")
    def test_three(self):
        pass

