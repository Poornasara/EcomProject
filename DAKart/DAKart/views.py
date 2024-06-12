from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from Store.models import Product


# Create your views here.

def greeting(request):  
    return render ("request, 'greet.html")

def WelcomeScreen(request):  
    products = Product.objects.all().filter(Is_available = True)
    
    context = {
        'products' : products       
    }
    
    return render(request, 'Welcome.html', context)

#def home(request):
    #return render(request, 'home.html')

#def aboutus(request):
    #return render(request, 'aboutus.html')

def ShowDetails(request):
    greet = { 'Welcome' : 'Hello User',
              'fname'   : 'Siddharth',
              'Gender'  : 'M',
              'Profile' : {'Job'     : 'Software Developer',
                           'Company' : 'Google'},
                           'Nos'    : [1,2,3,4,5]
                           }

    return render (request,'users.html', greet)

