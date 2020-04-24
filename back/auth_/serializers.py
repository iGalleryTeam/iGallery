from rest_framework import serializers
from auth_.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'username', 'is_moderator', 'first_name',)
