from django.http import Http404
from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated

from api.models import Picture, Gallery
from api.serializers import PictureShortSerializer, PictureFullSerializer, GalleryModelSerializer

from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.decorators import action
import logging

logger = logging.getLogger(__name__)

class GalleryListViewSet(mixins.ListModelMixin,
						 mixins.CreateModelMixin,
						 mixins.RetrieveModelMixin,
						 mixins.UpdateModelMixin,
						 mixins.DestroyModelMixin,
						 viewsets.GenericViewSet):

	def get_queryset(self):
		is_virtual = self.request.query_params.get('is_virtual', None)
		if is_virtual is True:
			return Gallery.virtual_gallery.all()
		elif is_virtual is False:
			return Gallery.not_virtual_gallery.all()
		else:
			return Gallery.objects.all()

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



class PictureListViewSet(mixins.ListModelMixin,
						 mixins.CreateModelMixin,
						 mixins.RetrieveModelMixin,
						 mixins.UpdateModelMixin,
						 mixins.DestroyModelMixin,
						 viewsets.GenericViewSet):
	queryset = Picture.objects.all()

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
