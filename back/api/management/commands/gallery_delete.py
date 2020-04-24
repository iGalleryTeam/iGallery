from django.core.management.base import BaseCommand
from datetime import datetime
import random

from api.models import Gallery


class Command(BaseCommand):
    help = 'Delete Gallery objects from the table'

    def add_arguments(self, parser):
        parser.add_argument('gallery_ids', nargs='+', help='Gallery ids for delete')

    def handle(self, *args, **kwargs):

        for gallery_id in kwargs['gallery_ids']:
            try:
                g = Gallery.objects.get(id=gallery_id)
                g.delete()
                self.stdout.write(self.style.SUCCESS("Gallery id: {} deleted successfully".format(gallery_id)))
            except Gallery.DoesNotExist as e:
                self.stdout.write(self.style.ERROR("Gallery id: {} does not exist!".format(gallery_id)))
