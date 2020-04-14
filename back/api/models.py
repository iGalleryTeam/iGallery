# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.


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
	year_of_publishing = models.IntegerField()
	likes = models.IntegerField(default=0)
	image = models.ImageField(default=None)

	objects = models.Manager()
	created_by_user = CreatedByUser()
	modern_art = ModernArt()
	classic_art = ClassicArt()

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


class VirtualGallery(models.Manager):
	def get_queryset(self):
		return self.filter(is_virtual=True)


class NotVirtualGallery(models.Manager):
	def get_queryset(self):
		return self.filter(is_virtual=False)


class Gallery(models.Model):
	name = models.CharField(max_length=255)
	address = models.CharField(max_length=255)
	date_of_opening = models.DateTimeField()
	is_virtual = models.BooleanField(default=True)
	picture = models.ForeignKey(Picture, on_delete=models.CASCADE)

	objects = models.Manager()
	virtual_gallery = VirtualGallery()
	not_virtual_gallery = NotVirtualGallery()

	class Meta:
		verbose_name = 'Gallery'
		verbose_name_plural = 'Galleries'

	def __str__(self):
		return '{}: {}'.format(self.id, self.name)

	def to_json(self):
		return {
			"id": self.id,
			"name": self.name,
			"address": self.address,
			"date_of_opening": self.date_of_opening,
			"picture": self.picture,
			"is_virtual": self.is_virtual
		}


