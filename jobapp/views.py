from __future__ import absolute_import
from django.shortcuts import render, HttpResponse
from ..core import mains
from . import mains
# Create your views here.

def index(requests):
    
    for i in mains:
        
        print(ji)
    
    context={
        'title':'This title',
        'company':'this company',
        'mains':ji
    }
    
    return render(requests, 'index.html', context=context)
    
    
def normal(request):
    
    return HttpResponse('this is normal')
    

