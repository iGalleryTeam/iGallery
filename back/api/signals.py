from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Gallery, Picture, Sculpture


@receiver(post_save, sender=Gallery)
def gallery_created(sender, instance, created, **kwargs):
    Picture.objects.create(gallery=instance, name='Picture')
    Sculpture.objects.create(gallery=instance, name='Sculpture')

