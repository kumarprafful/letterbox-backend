from letterbox.models import BaseModel
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from letterbox.fields import IdentifierField
from letterbox.utils.random import generate_random_id
from phonenumber_field.modelfields import PhoneNumberField
from timezone_field import TimeZoneField


class User(AbstractUser):
    phone = PhoneNumberField(unique=True)
    email = models.EmailField(_('Email Address'), max_length=254, unique=True)

    country = CountryField(default='IN')
    timezone = TimeZoneField(default='Asia/Kolkata',
                             choices_display='WITH_GMT_OFFSET')

    source = models.CharField(max_length=255, blank=True, null=True)

    @property
    def name(self):
        return self.get_full_name()

    @property
    def company(self):
        return Company.objects.get(users=self)


def generate_name_cp():
    return generate_random_id('CP')


class Company(BaseModel):
    name = IdentifierField(default=generate_name_cp)
    users = models.ManyToManyField('users.User', through='users.CompanyUser')
    company_name = models.CharField(max_length=255, blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name

    @property
    def has_newsletter(self):
        return self.newsletters.exists()


class CompanyUser(BaseModel):
    ADMIN = 'admin'

    DESIGNATION_CHOICE = (
        (ADMIN, 'Admin'),
    )

    company = models.ForeignKey('users.Company', on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    designation = models.CharField(
        choices=DESIGNATION_CHOICE, max_length=50, default=ADMIN)
