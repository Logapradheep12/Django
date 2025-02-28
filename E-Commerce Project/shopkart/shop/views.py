from django.shortcuts import render
from . models import *

# Create your views here.

def home(request):
    return render(request,"index.html")
def register(request):
    return render(request,"register.html")
def collections(request):
    catagory = Catagory.objects.filter(status=0)
    return render(request,"collections.html",{"catagory":catagory})