from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def index(request):
    #return HttpResponse('Home')
    return render(request, 'home/index.html')

def men_productgrid(request):
    return render(request,'home/men/productgrid.html')

def men_productlist(request):
    return render(request,'home/men/productlist.html')

def men_details(request):
    return render(request,'home/men/details.html')    

def women_productgrid(request):
    return render(request,'home/women/productgrid.html')

def women_productlist(request):
    return render(request,'home/women/productlist.html')

def contact(request):
    return render(request,'home/contact.html')


