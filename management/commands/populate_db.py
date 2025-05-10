from django.core.management.base import BaseCommand


class Command(BaseCommand):
    # help = 'Custom management command'

    def handle(self, *args, **option):
        self.stdout.write('Running custom commands...')