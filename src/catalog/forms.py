from django import forms
from models import Item, Application


class AddItemForm(forms.ModelForm):
    # honeyspot
    country = forms.CharField(required=False)

    class Meta:
        model = Item


class ApplicationForm(forms.ModelForm):
    # honeyspot
    country = forms.CharField(required=False)

    class Meta:
        model = Application
        exclude = ['item',]
