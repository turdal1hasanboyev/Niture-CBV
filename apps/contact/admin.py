from django.contrib import admin

from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    ordering = ('-created_at',)
    readonly_fields = ('id', 'created_at', 'updated_at',)
    list_display = (
        'id',
        'name',
        'email',
        'phone',
        'is_active',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'name',
        'email',
    )
    list_filter = (
        'is_active',
        'name',
    )
