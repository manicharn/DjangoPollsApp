from functools import partial
from msilib.schema import Class
from urllib import response
from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import GrocerySerializer
from .models import GroceryCart


# Create your views here.

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