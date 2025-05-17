from django.core.management.base import BaseCommand
from user.models import User
from products.models import Product
from orders.models import Order, OrderItem 
import random
from django.utils import lorem_ipsum
from decimal import Decimal


class Command(BaseCommand):
    help = 'Create application data'

    def handle(self, *args, **option):
        self.stdout.write('Running custom commands...')

        user = User.objects.filter(username='admin').first()
        if not user:
            user = User.objects.create_superuser(username='admin', email='admin@test.com', password='admin123')

        products = [
            Product(name='Canon A7 ', description='A digital Camera to capture all the moments',price=2285.0,stock=24),
            Product(name='Kivo Gari', description='Instant gari mix',price=5.0,stock=58),
            Product(name='Enter the Wu-Tang(36 Chambers)', description=lorem_ipsum.paragraph(),price=100.0,stock=24),
            Product(name='Watch', description='Digital watch from China',price=75.0,stock=4),
            Product(name='Celebration Station', description='A pack of mixed sweets',price=305.0,stock=2),
            Product(name='Dairy Milk', description='White chocolate',price=15.0,stock=31),
            Product(name='Fruits of the Loom (white shirts)', description=lorem_ipsum.paragraph(),price=5.0,stock=24),
            Product(name='Nico & Co', description=lorem_ipsum.paragraph(),price=5.0,stock=1),
        ]     
        # bulk create all products
        Product.objects.bulk_create(products)

        all_products = Product.objects.all()

        for _ in range(3):
            order = Order.objects.create(user=user)
            for product in random.sample(list(all_products), 2) :
                OrderItem.objects.create(
                    order=order, product=product, quantity=random.randint(1, 5)
                )  

        self.stdout.write(self.style.SUCCESS('Application data created'))
