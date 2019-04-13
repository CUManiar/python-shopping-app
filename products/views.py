from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Offer


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html',
        {'products': products})


def new(request):
    return HttpResponse("Its Chirag's Page!!")
