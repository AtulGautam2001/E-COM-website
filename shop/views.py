from urllib import request
from django.shortcuts import render
from .models import Product
from math import ceil
from django.http import HttpResponse

# Create your views here.
def index(request):
    products = Product.objects.all()
    print(products)
    # n = len(products)
    # nSlides = n//4 + ceil(n/4-n//4)  
    allProds = []
    catProds = Product.objects.values('category','id')
    cats = {item['category'] for item in catProds}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(products)
        nSlides = n//4 + ceil(n/4-n//4) 
        allProds.append([prod,range(1,nSlides),nSlides])

    #params={'no_of_slides':nslides,'range': range(1,nslides),'product': products}
    #allProds = [[products,range(1,nSlides),nSlides],[products,range(1,nSlides),nSlides]]
    params = {'allProds':allProds}
    return render(request, 'shop/index.html',params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return HttpResponse("We are at contact")

def tracker(request):
    return HttpResponse("We are at tracker")

def search(request):
    return HttpResponse("We are at search")

def productview(request):
    return HttpResponse("We are at product view")

def checkout(request):
    return HttpResponse("We are at checkout")