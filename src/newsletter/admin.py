from django.contrib import admin

from newsletter.models import Genre, Newsletter, NewsletterCampaign


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'identifier': ('title',), }
    list_display = ['title', ]
    fields = ['title', 'identifier']


class NewsletterCampaignInlineAdmin(admin.TabularInline):
    model = NewsletterCampaign
    autocomplete_fields = ['letter', ]
    search_fields = ['letter', ]


@admin.register(Newsletter)
class NewsLetterAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'frequency']
    inlines = [NewsletterCampaignInlineAdmin, ]
    autocomplete_fields = ['company', ]
