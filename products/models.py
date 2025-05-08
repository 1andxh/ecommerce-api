from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()


    @property
    def in_stock(self):
        if self.stock > 0:
            return True
        return False
    
    def __str__(self) -> str:
        return self.name
 