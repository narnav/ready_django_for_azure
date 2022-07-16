from django.shortcuts import render
from django.urls import reverse_lazy
from . import models
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin

from django.http import JsonResponse
from .models import Product
from rest_framework.decorators import api_view

# Create your views here.
def index(r):
    return JsonResponse({'test':"test"})
 
 
# desc ,price,prodName,createdTime, _id
@api_view(['GET','POST','DELETE','PUT'])
def products(request,id=-1):
    if request.method == 'GET':    #method get all
        if int(id) > -1: #get single product
            if int(id)> Product.objects.count(): return JsonResponse({"out of bounds array":"1111"})
            product= Product.objects.get(_id = id)
 
            return JsonResponse({
            "desc":product.desc,
            "price":product.price
            },safe=False)
        else: # return all
            res=[] #create an empty list
            for productObj in Product.objects.all(): #run on every row in the table...
                res.append({"desc":productObj.desc,
                "price":productObj.price,
               "id":productObj._id
                }) #append row by to row to res list
            return JsonResponse(res,safe=False) #return array as json response
    if request.method == 'POST': #method post add new row
        print(request.data['desc'])
        desc =request.data['desc']
        Product.objects.create(desc=request.data['desc'] ,price=request.data['price'])
        return JsonResponse({'POST':"test"})
    if request.method == 'DELETE': #method delete a row
        temp= Product.objects.get(_id = id)
        temp.delete()
        return JsonResponse({'DELETE': id})
    if request.method == 'PUT': #method delete a row
        temp=Product.objects.get(_id = id)
 
        temp.price =request.data['price']
        temp.desc =request.data['desc']
        temp.save()
 
        return JsonResponse({'PUT': id})
