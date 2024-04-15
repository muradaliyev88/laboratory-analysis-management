from django.shortcuts import render,redirect,HttpResponseRedirect
import segno
from hashlib import shake_256
import hashlib
from time import localtime
from pathlib import Path
import random
import numpy as np
from django.urls import reverse
from .forms import  *
from .models import *
from asgiref.sync import sync_to_async
import os
from barcode import EAN13 as brcode
from barcode.writer import ImageWriter
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

BASE_DIR = Path(__file__).resolve().parent.parent



def add_prefix2():   
    prefix = hashlib.sha1(f"{np.random.rand(50)}{localtime}".encode('utf-8')).hexdigest()
    return str(int(prefix, 16))[:13]  

def add_prefix():   
    prefix = shake_256(f"{np.random.rand(50)}{localtime}".encode('utf-8')).hexdigest(20)
    return prefix  

async def index(request):
    
    return render(request,"main.html",{})

async def barcode_view(request):

    query = Barcode.objects.all()
    
    return render(request,"barcode_view.html",{"query":query})

async def show_barcode(request,slug):
    
    return render(request,"show_barcode.html",{'slug':slug})

async def create_barcode(request):
    if request.method == 'POST':
        form = Barcode_Form(request.POST or None, request.FILES or None)
        
        if form.is_valid():           
                        
            sampled_by   = form.cleaned_data['sampled_by']
            unit         = form.cleaned_data['unit']
            sample_point = form.cleaned_data['sample_point']
            sample_type  = form.cleaned_data['sample_type']
            data_time    = form.cleaned_data['data_time']
            color        = request.POST.get('color')
            
            hash = add_prefix2()
            print(hash)
            bkbarcode = brcode(f'{hash}', writer=ImageWriter())
            bkbarcode.save(f"{BASE_DIR}/static/barcode_images/{hash}")
            
            form.instance.hashing_name = hash
            
            form.save()
            return redirect(f'/show_barcode/{hash}',hash,permanent=True)
    else:
        return render(request,"create_barcode.html",{})


async def qr_lists(request):
    
    query = QR.objects.all()
    
    
    return render(request,"qr_view.html",{"query":query})



async def show_qr(request,slug):
    
    return render(request,"show_qr.html",{'slug':slug})



async def create_qr(request):
    if request.method == 'POST':
        form = QR_Form(request.POST or None, request.FILES or None)
        
        if form.is_valid():           
                        
            sampled_by   = form.cleaned_data['sampled_by']
            unit         = form.cleaned_data['unit']
            sample_point = form.cleaned_data['sample_point']
            sample_type  = form.cleaned_data['sample_type']
            data_time    = form.cleaned_data['data_time']
            color        = request.POST.get('color')
            
            hash = add_prefix()
            qrcode = segno.make([{'sampled_by':sampled_by, 'unit':unit, 'sample_point':sample_point, 'sample_type':sample_type,'data_time':data_time}])
            qrcode.save(f"{BASE_DIR}/static/qr_images/{hash}.svg", scale=40,dark=color, light='#ffffff',)
            
            form.instance.hashing_name = hash
            
            form.save()
            return redirect(f'/show_qr/{hash}',hash,permanent=True)
    else:
        return render(request,"create_qr.html",{})



