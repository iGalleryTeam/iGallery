import os

from django.core.exceptions import ValidationError

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
