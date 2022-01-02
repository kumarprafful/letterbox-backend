from common.models import TimeStampedModel
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class Subscriber(TimeStampedModel):
    company = models.ForeignKey(
        "users.Company", on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField("common.Tag", blank=True)
    email = models.EmailField(max_length=254)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    phone = PhoneNumberField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    dob = models.DateField(_("Date of Birth"), blank=True, null=True)

    def __str__(self) -> str:
        return self.email
