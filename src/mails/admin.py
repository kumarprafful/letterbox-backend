from django.contrib import admin

from mails.models import EmailBalance, EmailSettings, SenderEmailAddress


class EmailBalanceInlineAdmin(admin.TabularInline):
    model = EmailBalance


class SenderEmailAddressInlineAdmin(admin.TabularInline):
    model = SenderEmailAddress


@admin.register(EmailSettings)
class EmailSettingsAdmin(admin.ModelAdmin):
    inlines = [EmailBalanceInlineAdmin, SenderEmailAddressInlineAdmin, ]
