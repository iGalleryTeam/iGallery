from django.core.management.base import BaseCommand

from api.models import Picture


class Command(BaseCommand):
    help = 'Delete Picture objects from the table'

    def add_arguments(self, parser):
        parser.add_argument('picture_ids', nargs='+', help='Picture ids for delete')

    def handle(self, *args, **kwargs):

        for picture_id in kwargs['picture_ids']:
            try:
                p = Picture.objects.get(id=picture_id)
                p.delete()
                self.stdout.write(self.style.SUCCESS("Picture id: {} deleted successfully".format(picture_id)))
            except Picture.DoesNotExist as e:
                self.stdout.write(self.style.ERROR("Picture id: {} does not exist!".format(picture_id)))
