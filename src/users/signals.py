from django.db.models.signals import pre_save
from django.dispatch import receiver
from letterbox.utils.random import random_alpha_id

from users.models import User


@receiver(signal=pre_save, sender=User)
def user_pre_save(instance, **kwargs):
    if instance.id is None:
        instance.username = random_alpha_id(16)
