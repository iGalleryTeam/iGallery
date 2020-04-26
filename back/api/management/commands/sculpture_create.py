from django.core.management.base import BaseCommand

from api.models import Gallery, Sculpture


def create_gallery(num=3):
    galleries = [Gallery(name='Gallery {}'.format(i))
                 for i in range(num)]

    Gallery.objects.bulk_create(galleries)


class Command(BaseCommand):
    help = 'Create fake date for Sculpture table'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Number of sculptures for creation')
        parser.add_argument('-p', '--prefix', type=str, help='Prefix string for new sculptures')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        prefix = kwargs.get('prefix')

        if not prefix:
            prefix = 'My'

        create_gallery(total)

        for i in range(total):
            s = Sculpture.objects.create(name=f'{prefix}_sculpture {i}')
            self.stdout.write(f'Sculpture {s.id} created')
