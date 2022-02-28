from django import forms
from .models import tododb


class todoform(forms.ModelForm):
    class Meta:
        model = tododb
        fields = ['name', 'prio', 'date']
