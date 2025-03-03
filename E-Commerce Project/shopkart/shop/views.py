from django.shortcuts import render,redirect,HttpResponse
from . models import *
from django.contrib import messages


def home(request):
    return render(request,"index.html")
def register(request):
    return render(request,"register.html")
def collections(request):
    catagory = Catagory.objects.filter(status=0)
    return render(request,"collections.html",{"catagory":catagory})


def collectionsview(request,name):
    if(Catagory.objects.filter(name=name,status=0)):
        products=Catagory.objects.filter(Catagory__name=name)
        return render(request,"index.html",{"products":products,"category_name":name})
    else:
        messages.warning(request," No Such Category Found ")
        return redirect('collections')
    
    
def product_detail(request,cname,pname):
    return redirect('collections') 
