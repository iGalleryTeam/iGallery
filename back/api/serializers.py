from rest_framework import serializers

from api.models import Gallery, Picture, Sculpture
from api.validators import validate_name, validate_likes, validate_published, validate_opened


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
    name = serializers.CharField(validators=[validate_name])
    likes = serializers.IntegerField(read_only=True, validators=[validate_likes])
    published = serializers.IntegerField(validators=[validate_published])
    gallery_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Picture
        fields = ('id', 'name', 'gallery_id', 'created_by',)


class SculptureShortSerializer(PictureShortSerializer):
    class Meta(PictureShortSerializer.Meta):
        model = Sculpture


class GalleryModelSerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators=[validate_name])
    opened = serializers.IntegerField(validators=[validate_opened])
    pictures = PictureShortSerializer(many=True, read_only=True)
    sculptures = SculptureShortSerializer(many=True, read_only=True)

    class Meta:
        model = Gallery
        fields = ('id', 'name', 'address', 'opened', 'is_virtual', 'pictures', 'sculptures')


class PictureFullSerializer(PictureShortSerializer):
    gallery = GalleryModelSerializer(read_only=True)

    class Meta(PictureShortSerializer.Meta):
        fields = PictureShortSerializer.Meta.fields + ('published', 'genre', 'likes', 'image', 'gallery',)


class SculptureFullSerializer(SculptureShortSerializer):
    gallery = GalleryModelSerializer(read_only=True)

    class Meta(SculptureShortSerializer.Meta):
        fields = SculptureShortSerializer.Meta.fields + ('published', 'material', 'likes', 'image', 'gallery',)
