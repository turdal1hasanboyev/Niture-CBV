from django.contrib import admin

from .models import SubEmail


class SubEmailAdmin(admin.ModelAdmin):
    ordering = (
        '-id',
    )
    list_display = (
        'id',
        'email',
        'is_active',
        'created_at',
        'updated_at',
    )
    readonly_fields = (
        'created_at',
        'updated_at',
        'id',
    )
    search_fields = ('email',)
    list_filter = ('is_active',)
    fieldsets = (
        ('Add Sub Email', {
            'fields': ('email', 'is_active',),
        }),
    )

admin.site.register(SubEmail, SubEmailAdmin)
