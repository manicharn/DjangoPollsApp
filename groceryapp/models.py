from msilib.schema import Class
from django.db import models

# Create your models here

class GroceryCart(models.Model):
    product_name=models.CharField(max_length=200)
    price=models.FloatField()
    quantity=models.PositiveIntegerField()

