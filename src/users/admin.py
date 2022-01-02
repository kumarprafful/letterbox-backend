from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import Company, CompanyUser, User


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('country', 'phone', 'timezone', 'username', 'password')}),
        *UserAdmin.fieldsets[1:],
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name',
                       'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions',
                       'last_login', 'date_joined'),
        }),
    )

    readonly_fields = ("username",)
    search_fields = ["phone", "first_name", "email",
                     "last_name", "username", "timezone"]

    list_display = ("username", "name", "phone", "email", "date_joined")
    ordering = ("-date_joined",)

    list_filter = (
        *UserAdmin.list_filter,
        ('country', admin.AllValuesFieldListFilter),
        ('timezone', admin.AllValuesFieldListFilter)
    )


admin.site.register(User, CustomUserAdmin)


class CompanyUserAdminInline(admin.TabularInline):
    model = CompanyUser
    extra = 0
    autocomplete_fields = ['user', ]


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    inlines = [CompanyUserAdminInline, ]
    search_fields = ['company', ]
