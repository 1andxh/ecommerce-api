# from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework import Response
from products.models import Product
from products.serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()