from django.db import models

from letterbox.models import BaseModel


class EmailSettings(BaseModel):
    company = models.OneToOneField('users.Company', on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Email Settings'

    def __str__(self) -> str:
        return f'{str(self.company)}'

    @property
    def balance_wallet(self):
        email_balance, _ = EmailBalance.objects.get_or_create(settings=self)
        return email_balance

    @property
    def sender_email_addresses(self):
        return SenderEmailAddress.objects.filter(settings=self)

    @property
    def sender_email_addresses_count(self):
        return self.sender_email_addresses.count()


class EmailBalance(BaseModel):
    settings = models.OneToOneField(
        'mails.EmailSettings', on_delete=models.CASCADE)
    balance = models.IntegerField(default=100)

    def __str__(self) -> str:
        return f'{str(self.settings.company)} - {self.balance}'


class SenderEmailAddress(BaseModel):
    settings = models.ForeignKey(
        'mails.EmailSettings', on_delete=models.CASCADE)
    sender_email = models.EmailField(max_length=255)
    sender_name = models.CharField(max_length=100, null=True)
    verified = models.BooleanField(default=False)
    active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{str(self.settings)}'
