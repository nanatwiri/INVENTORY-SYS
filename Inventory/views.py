from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
# takes requests and returns a response
# request handler


def add_product(request):
    return HttpResponse("product added successfully!")


def add_New_Category_to_product_List(request):
    return HttpResponse("Category added successfully!")
