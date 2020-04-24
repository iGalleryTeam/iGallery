from rest_framework import serializers
from api.models import Gallery, Picture, Sculpture


class PictureSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	name = serializers.CharField(required=True)
	likes = serializers.IntegerField(read_only=True)

	def create(self, validated_data):
		picture = Picture(**validated_data)
		picture.save()
		return picture

	def update(self, instance, validated_data):
		instance.name = validated_data.get('name', instance.name)
		instance.save()
		return instance


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


class PictureShortSerializer(serializers.ModelSerializer):
	id = serializers.IntegerField(read_only=True)
	name = serializers.CharField(required=True)
	likes = serializers.IntegerField(read_only=True)
	gallery_id = serializers.IntegerField(write_only=True)

	class Meta:
		model = Picture
		fields = ('id', 'name', 'likes', 'gallery_id', 'year_of_publishing', 'genre', 'created_by', 'image')

	def validate_name(self, value):
		if any(x in value for x in ['%', '&', '$', '^']):
			raise serializers.ValidationError('invalid character in name field')
		return value

	def validate_year_of_publishing(self, value):
		if value < 0 or value > 2020:
			raise serializers.ValidationError('invalid date_of_publishing of the picture')
		return value

	def validate_likes(self, value):
		if value < 0:
			raise serializers.ValidationError('invalid number of likes')
		return value


class SculptureShortSerializer(serializers.ModelSerializer):
	id = serializers.IntegerField(read_only=True)
	name = serializers.CharField(required=True)
	likes = serializers.IntegerField(read_only=True)
	gallery_id = serializers.IntegerField(write_only=True)

	class Meta:
		model = Sculpture
		fields = ('id', 'name', 'likes', 'gallery_id', 'year_of_publishing', 'material', 'created_by', 'image')

	def validate_name(self, value):
		if any(x in value for x in ['%', '&', '$', '^']):
			raise serializers.ValidationError('invalid character in name field')
		return value

	def validate_year_of_publishing(self, value):
		if value < 0 or value > 2020:
			raise serializers.ValidationError('invalid date_of_publishing of the picture')
		return value

	def validate_likes(self, value):
		if value < 0:
			raise serializers.ValidationError('invalid number of likes')
		return value


class GalleryModelSerializer(serializers.ModelSerializer):
	id = serializers.IntegerField(read_only=True)
	name = serializers.CharField(required=True)
	pictures = PictureShortSerializer(many=True, read_only=True)
	sculptures = SculptureShortSerializer(many=True, read_only=True)

	class Meta:
		model = Gallery
		fields = ('id', 'name', 'address', 'year_of_opening', 'is_virtual', 'pictures', 'sculptures')

	def validate_name(self, value):
		if any(x in value for x in ['%', '&', '$', '^']):
			raise serializers.ValidationError('invalid character in name field')
		return value

	def validate_year_of_opening(self, value):
		if value < 0:
			raise serializers.ValidationError('invalid date type')
		return value


class PictureFullSerializer(PictureShortSerializer):
	gallery = GalleryModelSerializer(read_only=True)

	class Meta(PictureShortSerializer.Meta):
		fields = PictureShortSerializer.Meta.fields + ('gallery', )


class SculptureFullSerializer(SculptureShortSerializer):
	gallery = GalleryModelSerializer(read_only=True)

	class Meta(SculptureShortSerializer.Meta):
		fields = SculptureShortSerializer.Meta.fields + ('gallery', )
