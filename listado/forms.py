from django import forms
from .models import Lista
from django.forms import ModelForm

class ListaForm(ModelForm):
    class Meta:
        model = Lista
        fields = ["nombre", "opinion", "email"]