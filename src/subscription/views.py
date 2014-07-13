# coding=utf8
import json
from django.contrib import messages

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from subscription.forms import SubscriptionForm, UnSubscriptionForm
from subscription.models import Subscription


def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            subscription = form.save(commit=False)
            subscription.save()
            messages.add_message(request, messages.INFO,
                                 u'Вы успешно подписаны на получение информации о новых вакансиях')
            return HttpResponseRedirect(reverse('home'))
        else:
            messages.add_message(request, messages.WARNING, u'Исправьте пожалуйста ошибки выделенные красным цветом')
    else:
        form = SubscriptionForm()

    return render(request, 'subscription/add.html', {'form': form})



def unsubscribe(request):
    if request.method == 'POST':
        form = UnSubscriptionForm(request.POST)
        if form.is_valid():
            try:
                s = Subscription.objects.get(email=form.cleaned_data['email'])
                s.delete()
                messages.add_message(request, messages.SUCCESS, u'Вы успешно отписались от новых вакансий!')
                return HttpResponseRedirect(reverse('home'))

            except Subscription.DoesNotExist:
                messages.add_message(request, messages.WARNING, u'Ваш email не найден в списке подписчиков')


        else:
            messages.add_message(request, messages.WARNING, u'Исправьте пожалуйста ошибки выделенные красным цветом')
    else:
        form = UnSubscriptionForm()

    return render(request, 'subscription/del.html', {'form': form})
