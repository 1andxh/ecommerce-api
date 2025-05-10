from rest_framework import serializers
from products.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['namme',
            'description'
            'price',
            'stock',
            ]
        
        def validate_price(self, value):
            if value <= 0:
                raise serializers.ValidationError("Price must be greater than 0") 
            return value
        
        def validate_stock(self, value):
            if value <= 0 :
                raise serializers.ValidationError("Product out of stock")
            return value
            
class ProductCreateSerializer(serializers.ModelSerializer):
    pass
            
class ProductUpdateSerializer(serializers.ModelSerializer):
    pass
        