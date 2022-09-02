from decimal import Clamped
from msilib.schema import Class
from django.shortcuts import render
from django.views import View
import json
from django.http import JsonResponse
from .models import CartData
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class ShoppingCart(View):
    def post(self,request):
        data=json.loads(request.body.decode("UTF-8"))
        product=data.get("product_name")
        price=data.get("price")
        quantity=data.get("quantity")

        product_data={
            'product_name':product,
            'price':price,
            'quantity':quantity,
        }
        cart_item=CartData.objects.create(**product_data)

        msg={'message':f'the product data has been added to the cart data with id {cart_item.id}'}

        return JsonResponse(msg)

#  we can use the below commented code here itself using the same route or create 
#  the another class and call the get method using different route

    # def get(self,request):
    #     items_count=CartData.objects.count()
    #     items=CartData.objects.all()
    #     list_items=[]
    #     for item in items:
    #         list_items.append({
    #             'product_name':item.product_name,
    #             'price':item.price,
    #             'quantity':item.quantity,
    #         })
    #     data={
    #         'items':list_items,
    #         'count':items_count,
    #     }
    #     return JsonResponse(data)

class GetcartData(View):
    def get(self,request):
        items_count=CartData.objects.count()
        items=CartData.objects.all()
        list_items=[]
        for item in items:
            list_items.append({
                'product_name':item.product_name,
                'price':item.price,
                'quantity':item.quantity,
            })
        data={
            'items':list_items,
            'count':items_count,
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt, name='dispatch')
class ShoppingCartUpdate(View):
    def patch(self,request,item_id):
        data=json.loads(request.body.decode("UTF-8"))
        cart_item=CartData.objects.get(id=item_id)
        cart_item.quantity=data["quantity"]
        cart_item.save()

        msg={"message":f"the cart item with id={item_id} is updated"}

        return JsonResponse(msg)


@method_decorator(csrf_exempt, name='dispatch')
class ShoppingCartDelete(View):
    def delete(self,request,item_id):
        data=json.loads(request.body.decode("UTF-8"))
        cart_item=CartData.objects.get(id=item_id)
        cart_item.delete()

        msg={"message":f"the cart item with id={item_id} is deleted"}
        
        return JsonResponse(msg)