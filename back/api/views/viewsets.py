import logging

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from api.models import Comment, Picture, Gallery, Sculpture
from api.permissions import IsModerator
from api.serializers import CommentSerializer, PictureShortSerializer, PictureFullSerializer, GalleryModelSerializer, \
    SculptureShortSerializer, SculptureFullSerializer, LikesSerializer

logger = logging.getLogger(__name__)


class GalleryViewSet(viewsets.ModelViewSet):
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
        gallery_id = self.kwargs.get('parent_lookup_gallery')
        if gallery_id:
            return Picture.objects.filter(gallery_id=gallery_id)
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

    @action(methods=['PATCH'], detail=True)
    def like(self, request, pk):
        serializer = LikesSerializer(self.get_object(), data={'likes': 0})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        logger.warning('Picture with id {} was liked'.format(pk))
        return Response({'message': 'you liked it!'}, status=status.HTTP_200_OK)


class SculptureViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        gallery_id = self.kwargs.get('parent_lookup_gallery')
        if gallery_id:
            return Sculpture.objects.filter(gallery_id=gallery_id)
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

    @action(methods=['PATCH'], detail=True)
    def like(self, request, pk):
        serializer = LikesSerializer(self.get_object(), data={'likes': 0})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        logger.warning('Sculpture with id {} was liked'.format(pk))
        return Response({'message': 'you liked it!'}, status=status.HTTP_200_OK)


class CommentViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        picture_id = self.kwargs.get('parent_lookup_picture')
        if picture_id:
            return Comment.objects.filter(picture_id=picture_id)
        return Comment.objects.filter(author=self.request.user)

    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return AllowAny(),
        return IsAuthenticated(),

    def perform_create(self, serializer):
        picture_id = self.kwargs.get('parent_lookup_picture')
        serializer.save(author=self.request.user, picture_id=picture_id)
        logger.info('Comment is created: {}'.format(serializer.instance))

    def perform_destroy(self, instance):
        instance.delete()
        logger.warning('Comment is deleted, {}'.format(instance))
