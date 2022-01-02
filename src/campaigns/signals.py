from django.dispatch import receiver
from django.db.models.signals import post_save

from campaigns.models import CampaignContent
from campaigns.utils import manage_content_after_creation


@receiver(post_save, sender=CampaignContent)
def campaign_content_post_save(sender, instance, created, **kwargs):
    if created:
        manage_content_after_creation(instance)
    pass
