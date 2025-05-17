from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from orders.models import Order, OrderItem
from orders.serializers import OrderSerializer, OrderItemSerializer
from rest_framework.decorators import api_view


# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()

@api_view(['GET'])
def order_list(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)