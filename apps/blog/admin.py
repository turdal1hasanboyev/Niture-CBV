from django.contrib import admin

from .models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    ordering = (
        'name',
    )
    list_display = (
        'id',
        'name',
        'image',
        'is_active',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'is_active',
    )
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'name',
    )
