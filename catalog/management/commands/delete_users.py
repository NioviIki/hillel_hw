from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('user_delete', type=int, nargs="+",
                            help="Creates a random user with username, email, password.")

    def handle(self, *args, **options):
        x = User.objects.filter(pk__in=options['user_delete'])
        if not x.filter(is_superuser=True).exists():
            x.delete()
