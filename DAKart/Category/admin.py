from django.contrib import admin
from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('Category_Name','Slug', 'Description',)
    prepopulated_fields = {'Slug': ('Category_Name',)}

# Register your models here.
admin.site.register(Category, CategoryAdmin)
