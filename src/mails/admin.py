from django.contrib import admin

from mails.models import EmailBalance, EmailSettings, SenderEmailAddress


class EmailBalanceInlineAdmin(admin.TabularInline):
    model = EmailBalance
    extra = 0


class SenderEmailAddressInlineAdmin(admin.TabularInline):
    model = SenderEmailAddress
    extra = 0


@admin.register(EmailSettings)
class EmailSettingsAdmin(admin.ModelAdmin):
    inlines = [EmailBalanceInlineAdmin, SenderEmailAddressInlineAdmin, ]
    autocomplete_fields = ['company', ]
    list_display = ['company', 'balance_wallet',
                    'sender_email_addresses_count']
