from django.db import models
from user.models import User
from products.models import Product
import uuid


class Order(models.Model):
    class StatusChoices(models.TextChoices):
        PENDING = 'Pending'
        CONFIRMED = 'Confirmed'
        CANCELLED = 'Cancelled'

    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    order_number = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=StatusChoices.choices, default=StatusChoices.PENDING)
    products = models.ManyToManyField(Product, through='OrderItem', related_name='orders')


    def __str__(self) -> str:
        return f"Order placed for {self.user}\nOrder: {self.order_id}"
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)
    # product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    @property
    def item_total(self):
        return self.product.price * self.quantity
    
    def __str__(self) -> str:
        return f"{self.quantity} x {self.product.name} in Order {self.order.order_id}"





