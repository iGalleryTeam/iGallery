import logging

from api.models import Picture, Gallery, Sculpture
from api.serializers import PictureShortSerializer, PictureFullSerializer, GalleryModelSerializer, \
							SculptureShortSerializer, SculptureFullSerializer

from rest_framework import viewsets

logger = logging.getLogger(__name__)


class GalleryViewSet(viewsets.ModelViewSet):
	def get_queryset(self):
		is_virtual = self.request.query_params.get('is_virtual', None)
		if self.action == 'list':
			if is_virtual is True:
				return Gallery.virtual_gallery.prefetch_related('pictures')
			elif is_virtual is False:
				return Gallery.not_virtual_gallery.prefetch_related('pictures')
		return Gallery.objects.all()

	"""def get_queryset(self):
		is_virtual = self.request.query_params.get('is_virtual', None)
		if is_virtual is True:
			return Gallery.virtual_gallery.all()
		elif is_virtual is False:
			return Gallery.not_virtual_gallery.all()
		else:
			return Gallery.objects.all()"""

	serializer_class = GalleryModelSerializer

	def perform_create(self, serializer):
		serializer.save()
		logger.debug('Gallery is created: {}'.format(serializer.instance))
		logger.info('Gallery is created: {}'.format(serializer.instance))

	def perform_update(self, serializer):
		logger.debug('Gallery is updated, ID: {}'.format(serializer.instance))
		logger.info('Gallery is updated, ID: {}'.format(serializer.instance))
		logger.warning('Gallery is updated, ID: {}'.format(serializer.instance))

	def perform_destroy(self, instance):
		logger.warning('Gallery is deleted, ID: {}'.format(instance))


class PictureViewSet(viewsets.ModelViewSet):
	def get_queryset(self):
		if self.action == 'list':
			return Picture.objects.select_related('gallery')
		return Picture.objects.all()

	def get_serializer_class(self):
		if self.action == 'list':
			return PictureShortSerializer
		if self.action == 'retrieve':
			return PictureFullSerializer
		return PictureShortSerializer

	def perform_create(self, serializer):
		serializer.save()
		logger.debug('Picture is created: {}'.format(serializer.instance))
		logger.info('Picture is created: {}'.format(serializer.instance))

	def perform_update(self, serializer):
		logger.debug('Picture is updated, ID: {}'.format(serializer.instance))
		logger.info('Picture is updated, ID: {}'.format(serializer.instance))
		logger.warning('Picture is updated, ID: {}'.format(serializer.instance))

	def perform_destroy(self, instance):
		logger.warning('Picture is deleted, ID: {}'.format(instance))


class SculptureViewSet(viewsets.ModelViewSet):
	def get_queryset(self):
		if self.action == 'list':
			return Sculpture.objects.select_related('gallery')
		return Sculpture.objects.all()

	def get_serializer_class(self):
		if self.action == 'list':
			return SculptureShortSerializer
		if self.action == 'retrieve':
			return SculptureFullSerializer
		return SculptureShortSerializer

	def perform_create(self, serializer):
		serializer.save()
		logger.debug('Sculpture is created: {}'.format(serializer.instance))
		logger.info('Sculpture is created: {}'.format(serializer.instance))

	def perform_update(self, serializer):
		logger.debug('Sculpture is updated, ID: {}'.format(serializer.instance))
		logger.info('Sculpture is updated, ID: {}'.format(serializer.instance))
		logger.warning('Sculpture is updated, ID: {}'.format(serializer.instance))

	def perform_destroy(self, instance):
		logger.warning('Sculpture is deleted, ID: {}'.format(instance))
