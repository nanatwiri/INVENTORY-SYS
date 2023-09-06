from django.shortcuts import render, redirect
from Inventory.models import Product
from .forms import ProductForm
from django.views.generic import TemplateView


def add_items(request):
    return render(request, "add_items.html")


def edit_item(request):
    return render(request, "edit_item.html")


def item_list(request):
    return render(request, "item_list.html")


def Inventory(request):
    return render(request, "Inventory.html")
