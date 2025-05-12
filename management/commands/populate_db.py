from django.core.management.base import BaseCommand
from user.models import User
from products.models import Product
from orders.models import Order, OrderItem 


class Command(BaseCommand):
    # help = 'Custom management command'

    def handle(self, *args, **option):
        self.stdout.write('Running custom commands...')
        