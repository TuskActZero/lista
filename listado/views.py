from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView
from django.urls import reverse_lazy
from .models import Lista
from .forms import ListaForm
# Create your views here.


# la lista capo

class Opinion(CreateView):
    model = Lista
    form_class = ListaForm
    template_name = 'home.html'
    success_url = 'lista'

class Lista(ListView):
    model = Lista
    template_name = 'lista.html'
    context_object_name = 'listado'
    queryset = Lista.objects.all()
    