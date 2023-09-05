from django.shortcuts import render, redirect
from Inventory.models import Product
from .forms import ProductForm
from django.views.generic import TemplateView

# Create


def add_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'add_item.html', {'form': form})

# Read


def item_list(request):
    items = Item.objects.all()
    return render(request, 'item_list.html', {'items': items})

# Update


def edit_item(request, pk):
    item = Item.objects.get(pk=pk)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm(instance=item)
    return render(request, 'edit_item.html', {'form': form})

# Delete


def delete_item(request, pk):
    Item.objects.get(pk=pk).delete()
    return redirect('item_list')


# testing.

class TestCRUD(TemplateView):
    def get(self, request):
        return render(request, 'test_crud.html')


def test_crud_operations(request):
    # CREATE
    item = Item.objects.create(
        name='Test Item', description='This is a test item.')

    # READ
    item_from_db = Item.objects.get(id=item.id)
    if item_from_db.name != 'Test Item':
        return HttpResponse('Failed in Read operation.')

    # UPDATE
    item_from_db.name = 'Updated Test Item'
    item_from_db.save()
    updated_item = Item.objects.get(id=item.id)
    if updated_item.name != 'Updated Test Item':
        return HttpResponse('Failed in Update operation.')

    # DELETE
    item_from_db.delete()
    try:
        Item.objects.get(id=item.id)
        return HttpResponse('Failed in Delete operation.')
    except Item.DoesNotExist:
        pass

    return HttpResponse('All CRUD operations succeeded.')
