from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Gallery, Picture
from api.serializers import PictureSerializer, GalleryModelSerializer


@api_view(['GET', 'POST'])
def picture_list(request, pk):
    try:
        list = Picture.objects.get(id=pk)
    except Picture.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        pictures = list.objects.all()
        serializer = PictureSerializer(pictures, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = PictureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'POST'])
def gallery_list(request):
    if request.method == 'GET':
        galleries = Gallery.objects.all()
        serializer = GalleryModelSerializer(galleries, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = GalleryModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
