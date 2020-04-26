from rest_framework import serializers

from api.models import Comment, Gallery, Picture, Sculpture
from api.validators import validate_name, validate_likes, validate_published, validate_opened
from auth_.serializers import AuthorSerializer


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

    class Meta:
        model = Picture
        fields = ('id', 'name', 'genre', 'published', 'likes', 'image',)


class SculptureShortSerializer(PictureShortSerializer):
    class Meta(PictureShortSerializer.Meta):
        model = Sculpture
        fields = ('id', 'name', 'material', 'published', 'likes', 'image',)


class GalleryModelSerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators=[validate_name])
    opened = serializers.IntegerField(validators=[validate_opened])

    class Meta:
        model = Gallery
        fields = ('id', 'name', 'address', 'opened', 'is_virtual',)


class PictureFullSerializer(PictureShortSerializer):
    gallery = GalleryModelSerializer(read_only=True)
    created_by = AuthorSerializer(read_only=True)

    class Meta(PictureShortSerializer.Meta):
        fields = PictureShortSerializer.Meta.fields + ('gallery', 'created_by',)


class SculptureFullSerializer(PictureFullSerializer):
    class Meta(SculptureShortSerializer.Meta):
        fields = SculptureShortSerializer.Meta.fields + ('gallery', 'created_by',)


class CommentSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    picture = PictureShortSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('text', 'picture', 'author',)


class LikesSerializer(serializers.Serializer):
    likes = serializers.IntegerField()

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        instance.like(validated_data.get('likes'))
        return instance
