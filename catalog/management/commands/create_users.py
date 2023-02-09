from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from faker import Faker


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('user_create', type=int, choices=range(1, 10),
                            help="Creates a random user with username, email, password.")

    def handle(self, *args, **options):
        fake = Faker()

        for i in range(options["user_create"]):
            User.objects.bulk_create([User(username=fake.unique.user_name(),
                                           email=fake.unique.email(),
                                           password=fake.unique.password())]
                                     )
