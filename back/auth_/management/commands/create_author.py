from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError

from auth_.models import Author


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='Username')
        parser.add_argument('password', type=str, help='Password')
        parser.add_argument('-m', '--moderator', action='store_true', help='Flag defining is_moderator permission')
        parser.add_argument('-n', '--name', type=str, help='User first name')

    def handle(self, *args, **options):
        username = options['username']
        password = options['password']
        is_moderator = options.get('moderator')
        first_name = options.get('name')

        if not first_name:
            first_name = ''

        try:
            user = Author.objects.create(username=username, password=password,
                                         is_moderator=is_moderator, first_name=first_name)
            self.stdout.write(self.style.SUCCESS(f'User with id {user.id} was created'))
        except IntegrityError:
            self.stdout.write(self.style.ERROR(f'Failed to create user with username {username}. '
                                               f'Unique constraint failed'))
