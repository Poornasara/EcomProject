from django.shortcuts import render
import json
import datetime
from .forms import OrderForm
from .models import Order
from Carts.models import CartItem
from Order.models import payment, OrderProduct
from Store.models import Product
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.http import JsonResponse
from django.conf import settings



# Create your views here.

def payments(request):

    body = json.loads(request.body)

    order = Order.objects.all().filter(user=request.user,is_ordered=False).last()
    
    paymentobject = payment(
        user = request.user,
        payment_id = body['transID'],
        payment_method = body['payment_method'],
        amount_paid = order.order_total,
        status = body['status']
    )

    paymentobject.save()

    order.payment = paymentobject
    order.is_ordered = True
    order.save()    

# Move the cart items to Order product table

    cart_items = CartItem.objects.filter(user=request.user,is_active=True)

    for item in cart_items:
        orderproduct = OrderProduct()
        orderproduct.order_id = order.id 
        orderproduct.payment = paymentobject 
        orderproduct.user_id = request.user.id
        orderproduct.product_id = item.product_id
        orderproduct.quantity = item.quantity   
        orderproduct.product_price = item.product.Price 
        orderproduct.ordered = True
        orderproduct.save()      
        

# Reduce the quantity of cart item.

        productObj = Product.objects.get(id = item.product_id)
        productObj.Stock = item.quantity
        productObj.save()

# Clear cart

    CartItem.objects.filter(user=request.user).delete()
       

# Send order completion mail to user

    mail_subject = "DAKart - Your Order is Placed"
    email_from = settings.EMAIL_HOST_USER
    message = render_to_string('order_received.html',{
                 'user':request.user,
                 'order':order                         
                 
    })
    to_email = [request.user.email,]
    send_mail(mail_subject,message,email_from,to_email)
    
    print(order.order_number)
    print(paymentobject.payment_id)

# Redirect to order complete page

    data = {
            'order_number':order.order_number,
            'transID':paymentobject.payment_id
    }

    return JsonResponse(data)     


def place_order(request,total=0, grand_total=0,tax=0):

    form =  OrderForm(request.POST)
    
    current_user = request.user
    cart_items = CartItem.objects.filter(user=current_user,is_active=True)
    for cart_item in cart_items:
            total += cart_item.product.Price * cart_item.quantity
    
    if total !=0:
          
        tax = (2*100)/total
        tax = round(tax,2)
        grand_total = total + tax
        grand_total = round(grand_total,2)

    if request.method == 'POST':
        if form.is_valid():
                    
                    data = Order()
                    data.user = current_user
                    data.first_name = form.cleaned_data['first_name']
                    data.last_name = form.cleaned_data['last_name']
                    data.email = form.cleaned_data['email']
                    data.phone = form.cleaned_data['phone']
                    data.address_line_1 = form.cleaned_data['address_line_1']
                    data.address_line_2 = form.cleaned_data['address_line_2']
                    data.city = form.cleaned_data['city']
                    data.state = form.cleaned_data['state']
                    data.country = form.cleaned_data['country']
                    data.order_note = form.cleaned_data['order_note']
                    data.order_total = grand_total
                    data.tax = tax
                    data.ip = request.META.get('REMOTE_ADDR')
                    data.save()

# Order number generation

                    yr = int(datetime.date.today().strftime('%Y'))
                    dt = int(datetime.date.today().strftime('%d'))
                    mt = int(datetime.date.today().strftime('%m'))
                    d = datetime.date(yr,mt,dt)
                    current_date = d.strftime('%Y%m%d')
                    data.order_number = current_date + str(data.id)
                    data.save()

                    order = Order.objects.filter(user=current_user,is_ordered=False).last()
                    context = {
                           'order':order,
                           'cart_items':cart_items,
                           'total':total,
                           'tax':tax,
                           'grand_total':grand_total
                    }

                    return render(request,'Payments.html',context)
        else:
               pass

def order_complete(request, order_products=None, sub_total=0):
      
      order_number = request.GET.get('order_number')
      transID = request.GET.get('payment_id')
       
      order = Order.objects.get(order_number = order_number, is_ordered=True) 
       

      try:                  
        order_products =  OrderProduct.objects.filter(order_id = order.id) 

      except:            
            pass
          
      paymentobj = payment.objects.get(payment_id = transID)    

      if order_products.count() > 1:
            
            for i in order_products:
                  sub_total += i.product_price * i.quantity
      else:
                  
            sub_total = order_products[0].product_price
            print (order_products[0].product.Product_Name,order_products[0].quantity,order_products[0].product_price)
      
      for item in order_products:
            print (item.product.Product_Name,item.quantity,item.product_price)

      context = {
         'order':order,
         'order_products' : order_products,
         'payment': paymentobj,
         'order_number':order_number,
         'transID' : transID,
         'sub_total' : sub_total
      }

      return render(request,'Order_Complete.html',context)  
      
      