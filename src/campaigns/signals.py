from django.dispatch import receiver
from django.db.models.signals import post_save

from campaigns.models import Campaign, CampaignContent
from campaigns.utils import manage_content_after_creation


@receiver(post_save, sender=Campaign)
def campaign_post_save(sender, instance, created, **kwargs):
    if created:
        if instance.campaign_type == Campaign.CAMPAIGN_TYPE_TEXT or instance.campaign_type == Campaign.CAMPAIGN_TYPE_HTML_CODE:
            CampaignContent.objects.get_or_create(
                campaign=instance, content_type=CampaignContent.CONTENT_HTML, index=0)
    pass


@receiver(post_save, sender=CampaignContent)
def campaign_content_post_save(sender, instance, created, **kwargs):
    if created:
        manage_content_after_creation(instance)
    return
