from rest_framework import serializers
from campaigns.serializers import CampaignSerializer

from newsletter.models import Genre, Newsletter


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['identifier', 'title', ]


class NewsletterSerializer(serializers.ModelSerializer):
    letters = CampaignSerializer(many=True, required=False)

    class Meta:
        model = Newsletter
        fields = '__all__'
