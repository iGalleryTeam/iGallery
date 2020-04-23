from api.models import Picture, Gallery
from api.serializers import PictureSerializer, GalleryModelSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class GalleryList(APIView):
	def get(self, request):
		galleries = Gallery.objects.all()
		serializer = GalleryModelSerializer(galleries, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def post(self, request):
		serializer = GalleryModelSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PictureList(APIView):
	def get(self, request):
		pictures = Picture.objects.all()
		serializer = PictureSerializer(pictures, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def post(self, request):
		serializer = PictureSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
