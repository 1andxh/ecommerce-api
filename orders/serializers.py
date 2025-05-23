from rest_framework import serializers
from orders.models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    order = serializers.PrimaryKeyRelatedField(read_only=True)
    product = serializers.CharField(source="order.products.name", read_only=True)
    class Meta:
        model = OrderItem
        fields = [
            'product',
            'quantity'
        ]
class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = [
            'order_id',
            'created_at',
            'status',
            'user',
            'order_items'
        ]

