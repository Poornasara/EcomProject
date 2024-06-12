from django.db import models
from Store.models import Product
from django.contrib.auth.models import User


# Create your models here.
class Cart(models.Model):
    Cart_Id    = models.CharField(max_length=200, blank=True)
    Date_Added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.Cart_Id
    
class CartItem(models.Model):
    user      = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    product   = models.ForeignKey(Product,on_delete=models.CASCADE)
    cart      = models.ForeignKey(Cart, on_delete=models.CASCADE,null=True)
    quantity  = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.product.Product_Name
    
    def get_subtotal(self):
        return self.product.Price * self.quantity