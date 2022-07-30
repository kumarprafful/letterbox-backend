from django.contrib.postgres.fields import CIEmailField, CICharField
from django.db import models
from django.utils.translation import gettext_lazy as _
from letterbox.fields import IdentifierField
from letterbox.models import BaseModel
from phonenumber_field.modelfields import PhoneNumberField
from django.template.defaultfilters import slugify


class Tag(BaseModel):
    identifier = IdentifierField()
    title = CICharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if self.identifier is None:
            self.identifier = slugify(self.title)
        super(Tag, self).save(*args, **kwargs)


class Subscriber(BaseModel):
    company = models.ForeignKey(
        "users.Company", on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField("subscribers.Tag", blank=True)
    email = CIEmailField(max_length=254)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    phone = PhoneNumberField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    dob = models.DateField(_("Date of Birth"), blank=True, null=True)

    def __str__(self) -> str:
        return self.email
