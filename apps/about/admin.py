from django.contrib import admin

from .models import About


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'image',
        'is_active',
        'created_at',
        'updated_at',
    )
    ordering = ('id',)
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'is_active',
    )
