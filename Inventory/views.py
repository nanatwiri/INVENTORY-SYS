from django.shortcuts import render, redirect
# Make sure this is correct; previously, you tried to import 'Product'
from Inventory.models import Products
from .forms import ProductForm
from django.views.generic import TemplateView


def add_items(request):
    form = ProductForm()
    # Fixed the syntax here
    return render(request, "add_items.html", {'form': form})


def edit_item(request):
    return render(request, "edit_item.html")


def item_list(request):
    return render(request, "item_list.html")


def Inventory(request):
    return render(request, "Inventory.html")
