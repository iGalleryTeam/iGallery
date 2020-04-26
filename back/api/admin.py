from __future__ import unicode_literals

from django.contrib import admin

from api.models import Gallery, Picture, Sculpture


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'opened', 'is_virtual',)
    search_fields = ('name', 'opened', 'is_virtual',)
    ordering = ('name', 'opened',)


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'published', 'genre', 'likes', 'created_by', 'gallery',)
    search_fields = ('name', 'published',)
    ordering = ('likes', 'name', 'published',)


@admin.register(Sculpture)
class SculptureAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'published', 'material', 'likes', 'created_by', 'gallery',)
    search_fields = ('name', 'published',)
    ordering = ('likes', 'name', 'published',)
