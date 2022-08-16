from itertools import product
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView


from core.models import Product


class ProductList(ListView):
    model = Product

class ProductCreate(CreateView):
    model = Product
    fields = ['name']
