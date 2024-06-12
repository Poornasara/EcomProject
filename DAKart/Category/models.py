from django.db import models

# Create your models here.

class Category(models.Model):

    Category_Name = models.CharField(max_length=100, unique=True)
    Slug          = models.CharField(max_length=100, unique=True)
    Description   = models.TextField(max_length=255)
    Cat_Image     = models.ImageField(verbose_name="Category Image",upload_to="photos/Categories", blank=True)

    class Meta():
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.Category_Name

