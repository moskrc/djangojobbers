# coding=utf8
import json
from django.contrib import messages
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from catalog.forms import AddItemForm, ApplicationForm
from catalog.models import Item


def index(request):
    items = Item.objects.all().order_by('-id')
    return render(request, 'catalog/index.html', {'items': items})


def view(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'catalog/view.html', {'item': item})


def feedback(request, item_id):
    item = get_object_or_404(Item, pk=item_id)

    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            if not form.cleaned_data['country']:
                new_feedback = form.save(commit=False)
                new_feedback.item = item
                new_feedback.save()

            return HttpResponse(json.dumps({'success': True, 'message': 'Success'}), content_type="application/json")
        else:
            return HttpResponse(json.dumps({'success': False, 'errors': form.errors}), content_type="application/json")


def add(request):
    if request.method == 'POST':
        form = AddItemForm(request.POST)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.save()
            messages.add_message(request, messages.SUCCESS,
                                 u'Ваше объявление успешно добавлено! Письмо со ссылкой для редактирования или удаления отправлена вам на email.')
            return HttpResponseRedirect(reverse('catalog_view', kwargs={'item_id': new_item.pk}))
        else:
            messages.add_message(request, messages.WARNING, u'Исправьте пожалуйста ошибки выделенные красным цветом')
    else:
        form = AddItemForm()

    return render(request, 'catalog/add.html', {'form': form})


def edit(request, item_id, secret_key):
    print item_id, secret_key
    items = Item.objects.all()
    return render(request, 'catalog/index.html', {'items': items})


def delete(request, item_id, secret_key):
    print item_id, secret_key
    items = Item.objects.all()
    return render(request, 'catalog/index.html', {'items': items})


def subscribe(request):
    items = Item.objects.all()
    return render(request, 'catalog/index.html', {'items': items})
