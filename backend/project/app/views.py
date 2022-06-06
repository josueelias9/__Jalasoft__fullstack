from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Order

import json
import requests

# Create your views here.

def param(request):
    param = 'milk'
    Order.objects.filter(pk=myRequest["key"]).update(first_name=myRequest["updatedName"])
    myResponse = {
        "info": "param endopoint response.",
        }
    return JsonResponse(myResponse, safe=False)

def dates(request):
    myResponse = {
        "info": "param endopoint response.",
        }
    return JsonResponse(myResponse, safe=False)

def accessToApi(request):
    if request.method == 'GET':
        response = requests.get("https://api.storerestapi.com/products")
        return JsonResponse(response.json(), safe=False)

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
            Order(products=asd).save()
            myResponse = {"info": "order created! :D"}
        except:
            myResponse = {"info": "The request is not in JSON format"}
    else:
        myResponse = {"info": "Bad method. Only POST allowed by this endpoint."}
        
    return JsonResponse(myResponse)