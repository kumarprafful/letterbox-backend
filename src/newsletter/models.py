from django.db import models
from letterbox.fields import IdentifierField
from letterbox.models import BaseModel
from letterbox.utils.random import generate_random_id


def generate_name_nl():
    return generate_random_id('NL')


class Genre(BaseModel):
    identifier = IdentifierField()
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Newsletter(BaseModel):
    DAILY = 'daily'
    WEEKLY = 'weekly'
    FORTNIGHTLY = 'fortnightly'
    MONTHLY = 'monthly'
    QUARTERLY = 'quarterly'
    SEMESTER = 'semester'
    YEARLY = 'yearly'
    OTHER = 'other'

    FREQUENCY_CHOICES = (
        (DAILY, 'Daily'),
        (WEEKLY, 'Weekly'),
        (FORTNIGHTLY, 'Fortnightly'),
        (MONTHLY, 'Monthly'),
        (QUARTERLY, 'Quarterly'),
        (SEMESTER, 'Semester'),
        (YEARLY, 'Yearly'),
        (OTHER, 'Other'),
    )

    company = models.ForeignKey(
        "users.Company", related_name="newsletters", on_delete=models.CASCADE)
    identifier = IdentifierField(default=generate_name_nl)
    title = models.CharField(max_length=255)
    genres = models.ManyToManyField("newsletter.Genre", blank=True)
    letters = models.ManyToManyField(
        "campaigns.Campaign", through="newsletter.NewsletterCampaign", blank=True)
    frequency = models.CharField(
        max_length=50, choices=FREQUENCY_CHOICES, default=OTHER)

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ['company', 'title', ]

    @property
    def total_letters_count(self):
        return self.letters.count()


class NewsletterCampaign(BaseModel):
    newsletter = models.ForeignKey(
        "newsletter.Newsletter", on_delete=models.CASCADE)
    letter = models.OneToOneField(
        "campaigns.Campaign", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{str(self.letter)} - {str(self.newsletter)}'
