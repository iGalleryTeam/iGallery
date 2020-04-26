import logging

from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from api.models import Picture, Gallery, Sculpture
from api.permissions import IsModerator
from api.serializers import PictureShortSerializer, PictureFullSerializer, GalleryModelSerializer, \
    SculptureShortSerializer, SculptureFullSerializer

logger = logging.getLogger(__name__)


class GalleryViewSet(viewsets.ModelViewSet):
    # def get_queryset(self):
    #     is_virtual = self.request.query_params.get('is_virtual', None)
    #     if is_virtual == 'true':
    #         return Gallery.virtual_galleries.all()
    #     elif is_virtual == 'false':
    #         return Gallery.non_virtual_galleries.all()
    #     return Gallery.objects.all()

    queryset = Gallery.objects.all()
    serializer_class = GalleryModelSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return AllowAny(),
        return IsAuthenticated(), IsModerator(),

    def perform_create(self, serializer):
        serializer.save()
        logger.info('Gallery is created: {}'.format(serializer.instance))

    def perform_destroy(self, instance):
        instance.delete()
        logger.warning('Gallery is deleted, {}'.format(instance))


class PictureViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        if self.action == 'list':
            return Picture.objects.select_related('gallery')
        return Picture.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PictureFullSerializer
        return PictureShortSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return AllowAny(),
        return IsAuthenticated(),

    def perform_create(self, serializer):
        gallery_id = self.kwargs.get('parent_lookup_gallery')
        serializer.save(created_by=self.request.user, gallery_id=gallery_id)
        logger.info('Picture is created: {}'.format(serializer.instance))

    def perform_destroy(self, instance):
        instance.delete()
        logger.warning('Picture is deleted, {}'.format(instance))


class SculptureViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        if self.action == 'list':
            return Sculpture.objects.select_related('gallery')
        return Sculpture.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return SculptureFullSerializer
        return SculptureShortSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return AllowAny(),
        return IsAuthenticated(),

    def perform_create(self, serializer):
        gallery_id = self.kwargs.get('parent_lookup_gallery')
        serializer.save(created_by=self.request.user, gallery_id=gallery_id)
        logger.info('Sculpture is created: {}'.format(serializer.instance))

    def perform_destroy(self, instance):
        instance.delete()
        logger.warning('Sculpture is deleted, {}'.format(instance))
