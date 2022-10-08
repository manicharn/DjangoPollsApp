from functools import partial
from msilib.schema import Class
from urllib import response
from django.shortcuts import render,get_object_or_404,redirect,HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import GrocerySerializer
from .models import GroceryCart
from .forms import MyForm


# Create your views here.
from django.views.generic import View

class ItemsTodatabaseApi(View):
    # template_name = "groceryapp/post_items.html"

    def get(self, request):
        form = MyForm()
        return render(request,"groceryapp/post_items.html", {"form": form})

    def post(self, request):
        form = MyForm(request.POST)
        if form.is_valid():
            # Do something with the form data
            item = form.cleaned_data['item']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            print(item,price,quantity)
            import requests
            import json

            url = "http://127.0.0.1:8000/shoppingapp/addcart/"

            payload = json.dumps({
                "product_name": item,
                "price": price,
                "quantity": quantity
            })
            headers = {
            'Content-Type': 'application/json'
            }

            response = requests.request("POST", url, headers=headers, data=payload)

            print(response.text)
            # print(form.cleaned_data)
            return redirect('items-to-database')
            # return HttpResponseRedirect(reverse("items-to-database"))
        return render(request, "groceryapp/post_items.html", {"form": form})


class GroceryCartViews(APIView):
    def post(self,request):
        serializer=GrocerySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success","data":serializer.data},status=status.HTTP_200_OK)
        else:
            return Response({"status":"error","data":serializer.errors},status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,id=None):
        if id:
            item=GroceryCart.objects.get(id=id)
            serializer=GrocerySerializer(item)
            return Response({"status":"success","data":serializer.data},status=status.HTTP_200_OK)

        items=GroceryCart.objects.all()
        serializer=GrocerySerializer(items,many=True)
        return Response({"status":"sucsess","data":serializer.data},status=status.HTTP_200_OK)

    def patch(self,request,id=None):
        item=GroceryCart.objects.get(id=id)
        serializer=GrocerySerializer(item,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success","data":serializer.data})
        else:
            return Response({"status":"error","data":serializer.errors})

    def delete(self,request,id=None):
        item=get_object_or_404(GroceryCart,id=id)
        item.delete()
        return Response({"status":"success","data":"Item deleted"})


class RenderingPages(APIView):
    def get(self,request):
        items=GroceryCart.objects.all()
        # serializer=GrocerySerializer(item)
        return render(request,'groceryapp/viewpage.html',{
            "items":items,
            "error":"Some thing went wrong",
        })