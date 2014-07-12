from django import forms
from models import Item


class AddItemForm(forms.ModelForm):
    class Meta:
        model = Item

class ItemFeedbackForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    about = forms.CharField()