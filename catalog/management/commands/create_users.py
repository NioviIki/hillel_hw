from faker import Faker
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('user_create', type=int, choices=range(1, 10))

    def handle(self, *args, **options):
        fake = Faker()

        list_of_fake = [[fake.unique.user_name(), fake.unique.email(), fake.unique.password()] for _ in range(options["user_create"])]
        self.stdout.write(self.style.SUCCESS(f'Successfully {options["user_create"]}, {list_of_fake}'))
