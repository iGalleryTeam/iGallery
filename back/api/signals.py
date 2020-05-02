from django.db.models.signals import post_save
from django.dispatch import receiver

from api.models import Gallery, Picture, Sculpture
from auth_.models import Author


@receiver(post_save, sender=Gallery)
def gallery_created(sender, instance, created, **kwargs):
    Picture.objects.create(gallery=instance, name='Picture', created_by=Author.objects.get(id=1))
    Sculpture.objects.create(gallery=instance, name='Sculpture', created_by=Author.objects.get(id=1))
