#coding=utf8

from django import forms
from models import Subscription


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        exclude = ['site',]

    def clean_email(self):
        data = self.cleaned_data['email']
        if Subscription.objects.filter(email=data).exists():
            raise forms.ValidationError(u"Вы уже подписаны на новые вакансии")

        return data

class UnSubscriptionForm(forms.Form):
    email = forms.EmailField()