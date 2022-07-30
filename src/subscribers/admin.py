from django.contrib import admin

from subscribers.models import Subscriber, Tag


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['company', 'email']
    search_fields = ['email', ]
    autocomplete_fields = ['company', ]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['identifier', 'title']
    prepopulated_fields = {'identifier': ('title',)}
