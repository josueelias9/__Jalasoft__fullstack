from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


from .models import Client, Order, Product

import json
import requests

# Create your views here.

def retrieveProductsFromApi(request):
    Product.objects.all().delete()
    responseFromApi = requests.get("https://api.storerestapi.com/products")
    json = responseFromApi.json()
    for x in json["data"]:
        # print(x["_id"])
        product = Product(api_key=x["_id"])
        product.save()
    response = {"info":"all elements in Product table were deleted. Updated with information retrieved from api."}
    return JsonResponse(response)

def param(request,slug):
    # Order.objects.filter(pk=myRequest["key"]).update(first_name=myRequest["updatedName"])
    myResponse = {
        "info": "param endopoint response.",
        "product":slug
        }
    return JsonResponse(myResponse, safe=False)

def dates(request):
    myResponse = {
        "info": "param endopoint response.",
        }
    return JsonResponse(myResponse, safe=False)

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