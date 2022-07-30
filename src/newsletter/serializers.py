from rest_framework import serializers
from campaigns.serializers import CampaignCreateSerializer, CampaignSerializer

from newsletter.models import Genre, Newsletter, NewsletterCampaign


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['identifier', 'title', ]


class NewsletterSerializer(serializers.ModelSerializer):
    letters = serializers.SerializerMethodField()

    class Meta:
        model = Newsletter
        fields = ['company', 'identifier', 'title', 'letters', 'genres',
                  'total_letters_count', 'total_subscribers_count', 'updated_at', 'created_at', ]

    def get_letters(self, obj):
        letters = obj.letters.order_by('updated_at')
        return CampaignSerializer(letters[:5], many=True).data


class NewsletterCampaignWriteSerializer(serializers.ModelSerializer):
    letter = CampaignCreateSerializer()
    newsletter_id = serializers.CharField(source='newsletter.identifier')

    class Meta:
        model = NewsletterCampaign
        fields = ['newsletter_id', 'letter']


class NewsletterCampaignSerializer(serializers.ModelSerializer):
    letter = CampaignSerializer()

    class Meta:
        model = NewsletterCampaign
        fields = ['letter', ]
