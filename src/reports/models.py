from django.db import models

from letterbox.models import BaseModel


class CampaignReport(BaseModel):
    campaign = models.ForeignKey(
        'campaigns.Campaign', on_delete=models.CASCADE)
