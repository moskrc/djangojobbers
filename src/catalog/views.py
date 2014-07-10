from django.shortcuts import render
from catalog.models import Item


def index(request):
    items = Item.objects.all()
    return render(request, 'catalog/index.html', {'items': items})


def view(request, item_id):
    items = Item.objects.all()
    return render(request, 'catalog/view.html', {'items': items})

def add(request):
    items = Item.objects.all()
    return render(request, 'catalog/index.html', {'items': items})

def edit(request, item_id):
    items = Item.objects.all()
    return render(request, 'catalog/index.html', {'items': items})

def delete(request, item_id):
    items = Item.objects.all()
    return render(request, 'catalog/index.html', {'items': items})

def subscribe(request):
    items = Item.objects.all()
    return render(request, 'catalog/index.html', {'items': items})
