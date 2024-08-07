from django import forms
from .models import *


class ComponentForm(forms.ModelForm):
    class Meta:
        model = Component
        fields = ['name', 'description', 'date_created', 'category', 'price', 'photo']
