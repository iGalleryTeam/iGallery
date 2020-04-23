# -*- coding: utf-8 -*-
from django.db import models
from utils.validators import validate_file_size, validate_extension


# Create your models here.


class VirtualGallery(models.Manager):
	def get_queryset(self):
		return self.filter(is_virtual=True)


class NotVirtualGallery(models.Manager):
	def get_queryset(self):
		return self.filter(is_virtual=False)


class Gallery(models.Model):
	name = models.CharField(max_length=255)
	address = models.CharField(max_length=255)
	year_of_opening = models.IntegerField(default=None)
	is_virtual = models.BooleanField(default=None)

	objects = models.Manager()
	virtual_gallery = VirtualGallery()
	not_virtual_gallery = NotVirtualGallery()

	class Meta:
		verbose_name = 'Gallery'
		verbose_name_plural = 'Galleries'

	def __str__(self):
		return '{}: {}'.format(self.id, self.name)


class CreatedByUser(models.Manager):
	def for_user(self, user):
		return self.filter(created_by=user)


class ModernArt(models.Manager):
	def get_queryset(self):
		return self.filter__gte(year_of_publishing=2000)


class ClassicArt(models.Manager):
	def get_queryset(self):
		return self.filter__lte(year_of_publishing=2000)


class Picture(models.Model):
	name = models.CharField(max_length=255)
	year_of_publishing = models.IntegerField(default=None, blank=True, null=True)
	likes = models.IntegerField(default=0)
	image = models.ImageField(upload_to='pictures', validators=[validate_file_size,
																validate_extension],
							  									default=None, null=True, blank=True)
	gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, default=None, null=True, blank=True,
								related_name='pictures')

	objects = models.Manager()
	created_by_user = CreatedByUser()

	class Meta:
		verbose_name = 'Picture'
		verbose_name_plural = 'Pictures'

	def __str__(self):
		return '{}: {}'.format(self.id, self.name)

	def to_json(self):
		return {
			"id": self.id,
			"name": self.name,
			"year_of_publishing": self.year_of_publishing,
			"likes": self.likes
		}




