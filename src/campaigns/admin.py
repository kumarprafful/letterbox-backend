from django.contrib import admin

from campaigns.models import (Campaign, CampaignContent, ContentImage, ContentSocialLink,
                              ContentStyle)


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    search_fields = ['title', 'identifier', ]
    list_display = ['title', 'identifier', 'campaign_type',
                    'is_template', 'created_at', 'updated_at', ]


class ContentImageTabularAdmin(admin.TabularInline):
    model = ContentImage
    extra = 0


class ContentStyleTabularAdmin(admin.TabularInline):
    model = ContentStyle
    extra = 0


class ContentSocialLinkAdmin(admin.TabularInline):
    model = ContentSocialLink
    extra = 0


@admin.register(CampaignContent)
class CampaignContentAdmin(admin.ModelAdmin):
    inlines = [ContentImageTabularAdmin,
               ContentStyleTabularAdmin, ContentSocialLinkAdmin]
    search_fields = ['campaign__identifier', 'campaign__title', ]
    autocomplete_fields = ['campaign', ]
