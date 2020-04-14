from rest_framework import serializers
from models import Gallery, Picture


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


class PictureModelSerializer(serializers.ModelSerializer):
	id = serializers.IntegerField(read_only=True)
	name = serializers.CharField(required=True)

	class Meta:
		model = Picture
		fields = '__all__'

	def validate_name(self, value):
		if['/', '^', '$', '%', '`'] in value:
			raise serializers.ValidationError('invalid character in name field')
		return value

	def validate_date_of_publishing(self, value):
		if value < 0 or value > 2020:
			raise serializers.ValidationError('invalid date_of_publishing of the picture')
		return value

	def validate_likes(self, value):
		if value < 0:
			raise serializers.ValidationError('invalid number of likes')
		return value


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


class GalleryShortSerializer(serializers.ModelSerializer):
	id = serializers.IntegerField(read_only=True)
	name = serializers.CharField(required=True)
	picture_id = serializers.IntegerField(write_only=True)

	class Meta:
		model = Gallery
		fields = ('id', 'name', 'address', 'date_of_opening', 'is_virtual', 'picture_id')

	def validate_name(self, value):
		if['/', '^', '$', '%'] in value:
			raise serializers.ValidationError('invalid character in name field')
		return value

	def validate_date_of_opening(self, value):
		if value < 0:
			raise serializers.ValidationError('invalid date type')
		return value



class GalleryFullSerializer(GalleryShortSerializer):
	picture = PictureSerializer(read_only=True)

	class Meta(GalleryShortSerializer.Meta):
		fields = GalleryShortSerializer.Meta.fields + ('picture', )


