from faker import Faker
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = "Creates a random user with username, email, password."
    def add_arguments(self, parser):
        parser.add_argument('user_create', type=int, choices=range(1, 10))

    def handle(self, *args, **options):
        fake = Faker()

        list_of_fake = [[fake.unique.user_name(), fake.unique.email(), fake.unique.password()] for _ in range(options["user_create"])]
        # self.stdout.write(self.style.SUCCESS(f'Successfully {options["user_create"]}, {list_of_fake}'))
        # self.stdout.write(f"{User.objects.create(username='pepa')}")
        for i in list_of_fake:
            self.stdout.write(f"{User.objects.create(username=i[0], email=i[1], password=i[2]),}")
