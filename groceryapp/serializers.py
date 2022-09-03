from dataclasses import fields
from email.policy import default
from pyexpat import model
from typing_extensions import Required
from rest_framework import serializers
from .models import GroceryCart

class GrocerySerializer(serializers.ModelSerializer):
    product_name=serializers.CharField(max_length=200)
    price=serializers.FloatField()
    quantity=serializers.IntegerField(required=False,default=1)
    class Meta:
        model=GroceryCart
        fields=('__all__')