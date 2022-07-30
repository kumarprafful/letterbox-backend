from django.contrib import admin

from newsletter.models import Genre, Newsletter, NewsletterCampaign, NewsletterSubscriber


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'identifier': ('title',), }
    list_display = ['title', ]
    search_fields = ['title', 'identifier']


class NewsletterCampaignInlineAdmin(admin.TabularInline):
    model = NewsletterCampaign
    autocomplete_fields = ['letter', ]
    search_fields = ['letter', ]
    extra = 0


class NewsletterSubscriberInlineAdmin(admin.TabularInline):
    model = NewsletterSubscriber
    autocomplete_fields = ['subscriber', ]
    search_fields = ['subscriber', ]
    extra = 0


@admin.register(Newsletter)
class NewsLetterAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'frequency',
                    'total_letters_count', 'total_subscribers_count', 'created_at', ]
    inlines = [NewsletterCampaignInlineAdmin,
               NewsletterSubscriberInlineAdmin, ]
    autocomplete_fields = ['company', ]
