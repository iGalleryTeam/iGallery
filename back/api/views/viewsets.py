from django.http import Http404
from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated

from api.models import Picture, Gallery
from api.serializers import PictureModelSerializer, GalleryShortSerializer, GalleryFullSerializer

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

	def get_serializer_class(self):
		if self.action == 'list':
			return GalleryShortSerializer
		if self.action == 'retrieve':
			return GalleryFullSerializer
		return GalleryShortSerializer

	def perform_create(self, serializer):
		serializer.save()
		if self.action == 'create':
			logger.debug('Gallery object created: {}'.format(serializer.instance))
		elif self.action == 'update':
			logger.debug('Gallery object updated: {}'.format(serializer.instance))
		elif self.action == 'destroy':
			logger.debug('Gallery object deleted: {}'.format(serializer.instance))




class PictureListViewSet(mixins.ListModelMixin,
						 mixins.CreateModelMixin,
						 mixins.RetrieveModelMixin,
						 mixins.UpdateModelMixin,
						 mixins.DestroyModelMixin,
						 viewsets.GenericViewSet):
	queryset = Picture.objects.all()
	serializer_class = PictureModelSerializer

	def perform_create(self, serializer):
		serializer.save()
		if self.action == 'create':
			logger.debug('Picture object created: {}'.format(serializer.instance))
		if self.action == 'update':
			logger.debug('Picture object updated: {}'.format(serializer.instance))
		if self.action == 'destroy':
			logger.debug('Picture object deleted: {}'.format(serializer.instance))
