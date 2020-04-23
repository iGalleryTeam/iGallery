from __future__ import unicode_literals

from django.contrib import admin

from api.models import Gallery, Picture


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'picture', 'year_of_opening', 'is_virtual',)
    search_fields = ('name', 'picture', 'year_of_opening', 'is_virtual',)
    ordering = ('name', 'year_of_opening',)


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'year_of_publishing', 'likes', 'image',)
    search_fields = ('name', 'year_of_publishing',)
    ordering = ('likes', 'name', 'year_of_publishing',)
