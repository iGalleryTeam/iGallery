from django.core.management.base import BaseCommand
from datetime import datetime
import random

from api.models import Sculpture


class Command(BaseCommand):
	help = 'Delete Sculpture objects from the table'

	def add_arguments(self, parser):
		parser.add_argument('sculpture_ids', nargs='+', help='Sculpture ids for delete')

	def handle(self, *args, **kwargs):

		for sculpture_id in kwargs['sculpture_ids']:
			try:
				s = Sculpture.objects.get(id=sculpture_id)
				s.delete()
				self.stdout.write(self.style.SUCCESS("Sculpture id: {} deleted successfully".format(sculpture_id)))
			except Sculpture.DoesNotExist as e:
				self.stdout.write(self.style.ERROR("Sculpture id: {} does not exist!".format(sculpture_id)))
