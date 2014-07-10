from django.shortcuts import render
from catalog.forms import AddItemForm
from catalog.models import Item


def index(request):
    items = Item.objects.all()
    return render(request, 'catalog/index.html', {'items': items})


def view(request, item_id):
    items = Item.objects.all()
    return render(request, 'catalog/view.html', {'items': items})

def add(request):

    if request.method == 'POST':
        form = AddItemForm(request.POST)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.save()
    else:
        form = AddItemForm()

    return render(request, 'catalog/add.html', {'form': form})

def edit(request, item_id):
    items = Item.objects.all()
    return render(request, 'catalog/index.html', {'items': items})

def delete(request, item_id):
    items = Item.objects.all()
    return render(request, 'catalog/index.html', {'items': items})

def subscribe(request):
    items = Item.objects.all()
    return render(request, 'catalog/index.html', {'items': items})
