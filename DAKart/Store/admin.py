from django.contrib import admin
from Store.models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('Product_Name', 'Slug', 'Description', 'Price', 'Images', 'Stock', 'Category', 'Created_date', 'Modified_date', 'Is_available')
    prepopulated_fields = {'Slug' : ('Product_Name',)}
admin.site.register(Product, ProductAdmin)
