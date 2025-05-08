from django.db import models
from user.models import User
from products.models import Product
import uuid


# STATUS_CHOICES = [
#     ("PENDING", "Pending"),
#     ("CONFIRMED", "Confirmed"),
#     ("CANCELLED", "Cancelled")
# ]
class Order(models.Model):
    class StatusChoices(models.TextChoices):
        PENDING = 'Pending'
        CONFIRMED = 'Confirmed'
        CANCELLED = 'Cancelled'

    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    order_number = models.CharField
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.Choices(choices=StatusChoices.choices, default=StatusChoices.PENDING)
    products = models.ManyToManyField(Product)


    def __str__(self) -> str:
        return f"Order placed for {self.user}\nOrder: {self.order_id}"
    




