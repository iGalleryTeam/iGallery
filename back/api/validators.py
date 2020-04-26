import os

from django.core.exceptions import ValidationError
from rest_framework import serializers

MAX_FILE_SIZE = 100000000000
ALLOWED_EXTENSIONS = ['.jpg', '.png']


def validate_file_size(value):
    if value.size > MAX_FILE_SIZE:
        raise ValidationError('max file size is: {}'.format(MAX_FILE_SIZE))


def validate_extension(value):
    split_ext = os.path.splitext(value.name)
    if len(split_ext) > 1:
        ext = split_ext[1]
        if not ext.lower() in ALLOWED_EXTENSIONS:
            raise ValidationError('not allowed file, valid extensions: {}'.format(ALLOWED_EXTENSIONS))


def validate_name(value):
    if any(bad_char in value for bad_char in ['%', '&', '$', '^']):
        raise serializers.ValidationError('invalid character in name field')
    return value


def validate_published(value):
    if not (0 <= value <= 2020):
        raise serializers.ValidationError('invalid art object publishing date')
    return value


def validate_likes(value):
    if value < 0:
        raise serializers.ValidationError('invalid number of likes')
    return value


def validate_opened(value):
    if not(0 <= value <= 2020):
        raise serializers.ValidationError('invalid gallery opening date')
    return value
