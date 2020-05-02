from django.db.models.signals import post_save
from django.dispatch import receiver

from auth_.models import Author
from api.models import Gallery


@receiver(post_save, sender=Author)
def author_created(sender, instance, created, **kwargs):
    if created:
        Gallery.objects.create(name='This is your first virtual gallery')
