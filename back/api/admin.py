# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Gallery, NotVirtualGallery, VirtualGallery, Picture, CreatedByUser, ModernArt, ClassicArt

# Register your models here.


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'address', 'picture', 'year_of_opening', 'is_virtual')
	search_fields = ('name', 'picture', 'year_of_opening', 'is_virtual')
	ordering = ('name', 'year_of_opening',)


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'year_of_publishing', 'likes', 'image')
	search_fields = ('name', 'year_of_publishing')
	ordering = ('likes', 'name', 'year_of_publishing')


