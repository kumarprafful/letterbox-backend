from django.db.models.signals import pre_save
from django.dispatch.dispatcher import receiver
from rest_framework.exceptions import ValidationError

from newsletter.models import NewsletterSubscriber


@receiver(pre_save, sender=NewsletterSubscriber)
def newsletter_subscribers_pre_save(instance, *args, **kwargs):
    nl_sub = NewsletterSubscriber.objects.filter(
        newsletter=instance.newsletter, subscriber__email=instance.subscriber.email).exists()
    if nl_sub:
        raise ValidationError(
            'Subscriber with this email already exists with this newsletter')
    return
