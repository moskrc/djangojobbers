from django import forms
from models import Item, Application


class AddItemForm(forms.ModelForm):
    # honeyspot
    country = forms.CharField(required=False)

    class Meta:
        model = Item
        exclude = ['secret_key', 'not_sended',]


class ApplicationForm(forms.ModelForm):
    # honeyspot
    country = forms.CharField(required=False)

    class Meta:
        model = Application
        exclude = ['item',]
