from django.core.management.base import BaseCommand

from api.models import Gallery, Picture


def create_gallery(num=3):
    galleries = [Gallery(name='Gallery {}'.format(i))
                 for i in range(num)]

    Gallery.objects.bulk_create(galleries)


class Command(BaseCommand):
    help = 'Create fake date for Picture table'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Number of pictures for creation')
        parser.add_argument('-p', '--prefix', type=str, help='Prefix string for new pictures')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        prefix = kwargs.get('prefix')

        if not prefix:
            prefix = 'My'

        create_gallery(total)

        for i in range(total):
            p = Picture.objects.create(name=f'{prefix}_picture {i}')
            self.stdout.write(f'Picture {p.id} created')
