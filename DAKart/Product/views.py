from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def ListProduct(request):
    context ={
        "Name" : "T-Shirt",
        "Size" : "Medium",
        "Dress": "Tops",
        "Color": "Blue",
        "size" : "XL",
        "Toy" : "Toy Train"
    }
    #return HttpResponse("List your Products here : ")
    return render(request,"Product.html", context)


def EditProduct(request):
    return HttpResponse("Edit your Products here : ")