from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def produits(request):
    return render(request, 'produits.html')

def contact(request):
    return render(request, 'contact.html')

def apropos(request):
    return render(request, 'a-propos.html')