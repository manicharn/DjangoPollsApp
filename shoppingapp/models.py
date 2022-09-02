from msilib.schema import Class
from django.db import models

# Create your models here

class CartData(models.Model):
    product_name=models.CharField(max_length=100)
    price=models.FloatField()
    quantity=models.PositiveIntegerField()

