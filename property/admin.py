from django.contrib import admin

from .models import Flat


class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['owner', 'town', 'address']
    readonly_fields = ['created_at']


admin.site.register(Flat, AuthorAdmin)