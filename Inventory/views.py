from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
# takes requests and returns a response
# request handler


def add_product(request):
    return HttpResponse("product added successfully!")
