from django.db import models
from Category.models import Category
from django.contrib.auth.models import User
from django.db.models import Avg,Count

# Create your models here.
class Product(models.Model):

    Product_Name   = models.CharField(max_length=200, unique=True)
    Slug           = models.SlugField(max_length=100, unique=True)
    Description    = models.TextField(max_length=500, blank=True)
    Price          = models.IntegerField()
    Images         = models.ImageField(upload_to="photos/Products", blank=True)
    Stock          = models.IntegerField()
    Category       = models.ForeignKey(Category,on_delete=models.CASCADE) 
    Created_date   = models.DateField(auto_now_add=True)
    Modified_date  = models.DateField(auto_now_add=True) 
    Is_available   = models.BooleanField(default=True)

    def __str__(self):
        return self.Product_Name
    
    def averageReview(self):
        reviews = ReviewRating.objects.filter(product=self, status=True).aggregate(average=Avg('rating'))
        avg = 0
        if reviews['average'] is not None:
            avg = float(reviews['average'])
        return avg
    
    def CountReview(self):
        reviews = ReviewRating.objects.filter(product=self, status=True).aggregate(count=Count('id'))
        count = 0
        if reviews['count'] is not None:
            count = int(reviews['count'])
        return count


class ReviewRating(models.Model):

    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user    = models.ForeignKey(User,on_delete=models.CASCADE)
    subject = models.CharField(max_length=100, blank=True)
    review  = models.TextField(max_length=500, blank=True)
    rating  = models.FloatField()
    status  = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject