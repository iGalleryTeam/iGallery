from django.db import models

from api.validators import validate_file_size, validate_extension
from auth_.models import Author


class VirtualGallery(models.Manager):
    def get_queryset(self):
        return self.filter(is_virtual=True)


class NonVirtualGallery(models.Manager):
    def get_queryset(self):
        return self.filter(is_virtual=False)


class CreatedByUser(models.Manager):
    def for_user(self, user):
        return self.filter(created_by=user)


class ModernArt(models.Manager):
    def get_queryset(self):
        return self.filter__gte(year_of_publishing=2000)


class ClassicalArt(models.Manager):
    def get_queryset(self):
        return self.filter__lt(year_of_publishing=2000)


class Gallery(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, default='Paris')
    opened = models.IntegerField(default=2020)
    is_virtual = models.BooleanField(default=True)

    objects = models.Manager()
    virtual_galleries = VirtualGallery()
    non_virtual_galleries = NonVirtualGallery()

    class Meta:
        verbose_name = 'Gallery'
        verbose_name_plural = 'Galleries'

    def __str__(self):
        return f'{self.id}: {self.name}'


class ArtObject(models.Model):
    name = models.CharField(max_length=255)
    likes = models.IntegerField(default=0)
    published = models.IntegerField(default=2020)
    created_by = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)

    objects = models.Manager()
    created_by_user = CreatedByUser()
    modern_objects = ModernArt()
    classical_objects = ClassicalArt()

    class Meta:
        abstract = True

    def to_json(self):
        return {
            'name': self.name,
            'published': self.published,
            'likes': self.likes
        }

    def like(self, value):
        self.likes += 1
        self.save()


class Picture(ArtObject):
    genre = models.CharField(max_length=255, default='Landscape')
    image = models.ImageField(upload_to='pictures', validators=[validate_file_size, validate_extension],
                              null=True, blank=True)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name='pictures')

    class Meta:
        verbose_name = 'Picture'
        verbose_name_plural = 'Pictures'

    def __str__(self):
        return f'{self.id}: {self.name}'


class Sculpture(ArtObject):
    material = models.CharField(max_length=255, default='Stone')
    image = models.ImageField(upload_to='sculptures', validators=[validate_file_size, validate_extension],
                              null=True, blank=True)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name='sculptures')

    class Meta:
        verbose_name = 'Sculpture'
        verbose_name_plural = 'Sculptures'

    def __str__(self):
        return f'{self.id}: {self.name}'


class Comment(models.Model):
    text = models.TextField(max_length=300, default='')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='comments')
    picture = models.ForeignKey(Picture, on_delete=models.CASCADE, related_name='comments')

    objects = models.Manager()

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return f'{self.id}: {self.text[:20]}'
