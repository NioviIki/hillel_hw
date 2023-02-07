from django.test import TestCase

from django.contrib.auth.models import User
from catalog.management.commands.create_users import Command

class UserModelTests(TestCase):

    def test_a_user_has_been_created_or_not(self):

        """Пробует создать 5 пользователей"""

        test_create = Command()
        test_create.handle(user_create=5)

        self.assertIs(User.objects.exists(), True)



