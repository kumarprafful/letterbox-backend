from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from letterbox.fields import IdentifierField
from letterbox.models import BaseModel
from letterbox.utils.random import generate_random_id
from phonenumber_field.modelfields import PhoneNumberField
from timezone_field import TimeZoneField


class UserManager(BaseUserManager):
    def _create_user(self, email, password, *args, **kwargs):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(email=email, *args, **kwargs)
        user.set_password(password)
        user.save()
        return user
    
    def create_user(self, email, password, *args, **kwargs̵):
        kwargs̵.setdefault('is_staff', False)
        kwargs̵.setdefault('is_superuser', False)
        kwargs̵.setdefault('is_active', True)
        return self._create_user(email, password, *args, **kwargs̵)

    def create_superuser(self, email, password, *args, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)

        if kwargs.get('is_staff') is not True:
            raise ValueError('superuser must be a staff')
        if kwargs.get('is_superuser') is not True:
            raise ValueError('superuser must be a superuser')
        return self._create_user(email, password, *args, **kwargs)




class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    is_staff = models.BooleanField(_('staff_status'),  default=False)
    is_active = models.BooleanField(_('active'), default=True)

    phone = PhoneNumberField(unique=True, null=True)
    email = models.EmailField(_('Email Address'), unique=True)
    username = models.CharField(max_length=100, unique=True, blank=True)

    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)

    date_joined = models.DateTimeField(default=timezone.now)
    is_email_verified = models.BooleanField(default=False)
    is_phone_verified = models.BooleanField(default=False)

    country = CountryField(default='IN')
    timezone = TimeZoneField(default='Asia/Kolkata',
                             choices_display='WITH_GMT_OFFSET')

    source = models.CharField(max_length=255, blank=True, null=True)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = generate_random_id('U')
        return super().save(*args, **kwargs)

    def get_full_name(self):
        full_name = ''
        if self.first_name:
            full_name += self.first_name + ' '
        if self.last_name:
            full_name += self.last_name
        return full_name.strip() or None
    
    def set_full_name(self, name):
        parts = name.split(' ')
        if len(parts) < 1:
            return
        self.first_name = parts[0] if parts[0] else None
        last_name = ' '.join(parts[1:])
        self.last_name = last_name if last_name.strip() else None

    name = property(get_full_name, set_full_name)

    @property
    def company(self):
        return Company.objects.get(users=self)


def generate_name_cp():
    return generate_random_id('CP')


class Company(BaseModel):
    identifier = IdentifierField(default=generate_name_cp)
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
