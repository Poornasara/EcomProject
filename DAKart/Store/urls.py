from . import views
from django.urls import include, path

urlpatterns = [
    path('',views.Store,name='Store'),
    path('category/<slug:category_url>', views.Store, name='products_by_category'),
    path('category/<slug:category_url>/<slug:product_url>', views.Product_detail, name="product_details"),
    path('search/',views.search,name='search'),
    path('submit_review/<int:product_id>',views.submit_review,name='myrating'),
    
] 
