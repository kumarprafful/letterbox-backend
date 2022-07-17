from rest_framework import serializers

from campaigns.models import Campaign, CampaignContent, ContentImage, ContentSocialLink, ContentStyle


class ContentStyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentStyle
        fields = ['style_type', 'style_value', ]


class ContentImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentImage
        fields = ['image', 'alt_text', 'url', ]


class ContentSocialLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentSocialLink
        fields = ['social_type', 'url', ]


class CampaignContentSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    styles = serializers.SerializerMethodField()
    social_links = serializers.SerializerMethodField()

    class Meta:
        model = CampaignContent
        exclude = ['campaign', 'created_at', 'updated_at', ]

    def get_images(self, obj):
        if not obj.image_type:
            return None
        return ContentImageSerializer(obj.images, many=True).data if obj.images else None

    def get_styles(self, obj):
        return ContentStyleSerializer(obj.styles, many=True).data

    def get_social_links(self, obj):
        if obj.content_type != CampaignContent.SOCIAL_LINKS:
            return None
        return ContentSocialLinkSerializer(obj.social_links, many=True).data if obj.social_links else None


class CampaignCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = ['identifier', 'company', 'title', 'subject',
                  'preview_line', 'campaign_type', 'is_template', ]


class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = ['identifier', 'title', 'subject', 'preview_line',
                  'campaign_type', 'created_at', 'updated_at', ]


class CampaignContentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampaignContent
        fields = ['id', 'campaign', 'index', 'content_type', 'text', 'url']
