# from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework import response
from django.http import JsonResponse
from products.models import Product
from products.serializers import ProductSerializer

# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()

def product_list():
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return JsonResponse({
        'data' : serializer.data
    })