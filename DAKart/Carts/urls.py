from .import views
from django.urls import path

urlpatterns = [
    path('', views.Carts, name="cart"),
    path('add_cart/<int:product_id>/', views.add_cart,name="addcart"),
    path('remove_cart_item/<int:product_id>/', views.remove_cartItem,name="RemovecartItem"),
    path('checkout',views.checkout, name='checkout'),
    

]