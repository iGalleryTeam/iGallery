from rest_framework import serializers
from models import Gallery, Picture


class GallerySerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	name = serializers.CharField(required=True)

	def create(self, validated_data):
		gallery = Gallery(**validated_data)
		gallery.save()
		return gallery

	def update(self, instance, validated_data):
		instance.name = validated_data.get('name', instance.name)
		instance.save()
		return instance


class GallerySerializer2(serializers.ModelSerializer):
	id = serializers.IntegerField(read_only=True)
	name = serializers.CharField(required=True)

	class Meta:
		model = Gallery
		fields = '__all__'


class PictureSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	name = serializers.CharField(required=True)

	def create(self, validated_data):
		picture = Picture(**validated_data)
		picture.save()
		return picture

	def update(self, instance, validated_data):
		instance.name = validated_data.get('name', instance.name)
		instance.save()
		return instance


class PictureSerializer2(serializers.ModelSerializer):
	id = serializers.IntegerField(read_only=True)
	name = serializers.CharField(required=True)

	class Meta:
		model = Picture
		fields = '__all__'
