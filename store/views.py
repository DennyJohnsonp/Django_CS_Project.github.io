from django.shortcuts import render
from django.http import HttpResponse  
from .models.product import Product


def index(request):
    return render(request,'index.html')

def gallery(request):
    return render(request,'gallery.html')

def cart(request):
    prds = Product.get_all_products();
    return render(request,'cart.html',{'products':prds})

def cart2(request):
    prds = Product.get_all_products();
    return render(request,'cart2.html',{'products':prds})

