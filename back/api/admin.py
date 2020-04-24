from __future__ import unicode_literals

from django.contrib import admin

from api.models import Gallery, Picture, Sculpture


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'year_of_opening', 'is_virtual',)
    search_fields = ('name', 'picture', 'year_of_opening', 'is_virtual',)
    ordering = ('name', 'year_of_opening', 'is_virtual')


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'year_of_publishing', 'genre', 'likes', 'image', 'gallery', 'created_by',)
    search_fields = ('name', 'year_of_publishing', 'gallery')
    ordering = ('likes', 'name', 'year_of_publishing',)


@admin.register(Sculpture)
class SculptureAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'year_of_publishing', 'material', 'likes', 'image', 'gallery', 'created_by',)
    search_fields = ('name', 'year_of_publishing', 'gallery')
    ordering = ('likes', 'name', 'year_of_publishing',)
