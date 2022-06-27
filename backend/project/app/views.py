from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Order, Product

import json
import requests

# Create your views here.
# oooooooooooooooooooooooooooooooooooooooooooooooooooo
def retrieveProductsFromApi(request):
    Product.objects.all().delete()
    responseFromApi = requests.get("https://api.storerestapi.com/products")
    json = responseFromApi.json()

    for x in json["data"]:
        product = Product(api_key=x["_id"], product_name=x["title"])
        product.save()
    response = {"info":"All elements in Product table were deleted. Updated with information retrieved from api."}
    return JsonResponse(response)
# oooooooooooooooooooooooooooooooooooooooooooooooooooo
def param(request,str):
    products = list(Product.objects.all())
    productsFil = []
    for product in products:
        if(str in product.product_name):
            productsFil.append(product.api_key)
    myResponse = {
        "info": "param endopoint response.",
        "product":productsFil
        }
    return JsonResponse(myResponse)
# oooooooooooooooooooooooooooooooooooooooooooooooooooo
def dates(request):
    myResponse = {
        "info": "param endopoint response.",
        }
    return JsonResponse(myResponse)
# oooooooooooooooooooooooooooooooooooooooooooooooooooo
@csrf_exempt
def productbought(request):
    myResponse = dict()
    # ====================
    if request.method == 'GET':
        if len(list(Order.objects.values())) == 0:
            myResponse = {
                "info": "there is nothing in the data base",
            }
        else:        
            myResponse = {
                "info": "we send all the information",
                "data": []
            }
            myResponse["data"] = list(Order.objects.values())
    # ====================
    else:
        myResponse = {
            "info": "Bad method. This API only work with get method.",
        }
    return JsonResponse(myResponse, safe=False)
# oooooooooooooooooooooooooooooooooooooooooooooooooooo
@csrf_exempt
def order(request):
    myResponse = dict()
    if request.method == 'POST':
        try:
            asd = json.loads(request.body)
            print(asd["products"])
            order = Order()
            order.save()
            try:
                for x in asd["products"]:
                    product = Product.objects.get(api_key=x)
                    order.product.add(product)
                myResponse = {"info": "order created! :D"}
                return JsonResponse(myResponse)
            except:
                myResponse = {"info": "there is something wrong with the keys that you provide. Check it."}
                return JsonResponse(myResponse)
        except:
            myResponse = {"info": "The request is not in JSON format"}
            return JsonResponse(myResponse)
    else:
        myResponse = {"info": "Bad method. Only POST allowed by this endpoint."}        
        return JsonResponse(myResponse)