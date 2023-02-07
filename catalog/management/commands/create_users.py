from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('poll_ids', nargs='?')

    def handle(self, *args, **options):
            self.stdout.write(self.style.SUCCESS('Successfully'))