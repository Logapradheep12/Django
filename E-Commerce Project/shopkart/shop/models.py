from django.db import models
import datetime
import os

def getFileName(request,filename):
    now_time = datetime.datetime.now(). strftime("%Y%m%d%H:%M:%S")
    new_filename = "%s%s"%(now_time,filename)
    return os.path.join('upload/',new_filename)
    
    
class Catagory(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to=getFileName) 
    description = models.TextField(max_length=150, null=False, blank=False)
    status = models.BooleanField(default=False,help_text='0-show,1-Hidden')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Catagory,on_delete=models.CASCADE)
    name = models.CharField(max_length=150, null=False, blank=False)
    vendor = models.CharField(max_length=150, null=False, blank=False)
    product_imgage = models.ImageField(upload_to=getFileName) 
    quality = models.IntegerField(null=False, blank=False)
    original_price = models.IntegerField(null=False, blank=False)
    selling_price = models.IntegerField(null=False, blank=False)
    description = models.TextField(max_length=150, null=False, blank=False)
    status = models.BooleanField(default=False,help_text='0-show,1-Hidden')
    tranding = models.BooleanField(default=False,help_text='0-show,1-Tranding')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
