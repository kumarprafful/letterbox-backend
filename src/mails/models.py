from django.db import models

from common.models import TimeStampedModel


class EmailSettings(TimeStampedModel):
    company = models.OneToOneField('users.Company', on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Email Settings'

    @property
    def balance_wallet(self):
        return EmailBalance.objects.get(settings=self)

    @property
    def sender_email_addresses(self):
        return SenderEmailAddress.objects.filter(settings=self)


class EmailBalance(TimeStampedModel):
    settings = models.OneToOneField(
        'mails.EmailSettings', on_delete=models.CASCADE)
    balance = models.IntegerField(default=100)


class SenderEmailAddress(TimeStampedModel):
    settings = models.ForeignKey(
        'mails.EmailSettings', on_delete=models.CASCADE)
    sender_email = models.EmailField(max_length=255)
    sender_name = models.CharField(max_length=100, null=True)
    verified = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
