import logging

from rest_framework import viewsets

from api.models import Picture, Gallery, Sculpture
from api.serializers import PictureShortSerializer, PictureFullSerializer, GalleryModelSerializer, \
    SculptureShortSerializer, SculptureFullSerializer

logger = logging.getLogger(__name__)


class GalleryViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        is_virtual = self.request.query_params.get('is_virtual', None)
        if is_virtual is True:
            return Gallery.virtual_galleries.all()
        elif is_virtual is False:
            return Gallery.non_virtual_galleries.all()
        return Gallery.objects.all()

    serializer_class = GalleryModelSerializer

    def perform_create(self, serializer):
        serializer.save()
        logger.info('Gallery is created: {}'.format(serializer.instance))

    def perform_update(self, serializer):
        logger.info('Gallery is updated, ID: {}'.format(serializer.instance))

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
        logger.info('Picture is created: {}'.format(serializer.instance))

    def perform_update(self, serializer):
        logger.info('Picture is updated, ID: {}'.format(serializer.instance))

    def perform_destroy(self, instance):
        logger.warning('Picture is deleted, ID: {}'.format(instance))


class SculptureViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        if self.action == 'list':
            return Sculpture.objects.select_related('gallery')
        return Sculpture.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return SculptureFullSerializer
        return SculptureShortSerializer

    def perform_create(self, serializer):
        serializer.save()
        logger.info('Sculpture is created: {}'.format(serializer.instance))

    def perform_update(self, serializer):
        logger.info('Sculpture is updated, ID: {}'.format(serializer.instance))

    def perform_destroy(self, instance):
        logger.warning('Sculpture is deleted, ID: {}'.format(instance))
