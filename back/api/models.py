# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.


class Gallery(models.Model):
	name = models.CharField(max_length=255)
	address = models.CharField(max_length=255)
	year = models.DateTimeField()
	virtual = models.BooleanField(default=True)

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
			"year": self.year,
			"virtual": self.virtual
		}


class Picture(models.Model):
	name = models.CharField(max_length=255)
	year = models.DateTimeField()
	gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name='pictures')
	likes = models.IntegerField(default=0)
	image = models.ImageField(default=None)

	class Meta:
		verbose_name = 'Picture'
		verbose_name_plural = 'Pictures'

	def __str__(self):
		return '{}: {}'.format(self.id, self.name)

	def to_json(self):
		return {
			"id": self.id,
			"name": self.name,
			"year": self.year,
			"gallery": self.gallery,
			"likes": self.likes
		}

