from django import forms
from .models import Items, ListItems


class ItemsForms(forms.ModelForm):
    class Meta:
        model = Items
        fields = '__all__'