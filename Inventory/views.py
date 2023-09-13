from django.shortcuts import render, redirect
# Make sure this is correct; previously, you tried to import 'Product'
from Inventory.models import Products
from .forms import ProductForm
from django.views.generic import TemplateView


def add_items(request):
<<<<<<< HEAD
    form = ProductForm()
    # Fixed the syntax here
    return render(request, "add_items.html", {'form': form})


def edit_item(request):
    return render(request, "edit_item.html")


def item_list(request):
    return render(request, "item_list.html")


def Inventory(request):
    return render(request, "Inventory.html")
=======
    return render(request, "Inventory/add_items.html")


def edit_item(request):
    return render(request, "Inventory/edit_item.html")


def item_list(request):
    return render(request, "Inventory/item_list.html")


def Inventory(request):
    return render(request, "Inventory/Inventory.html")
>>>>>>> f6303f82dd2423d6f049b97293102b7614ac5f73
