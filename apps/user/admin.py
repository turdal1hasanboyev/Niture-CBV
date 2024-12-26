from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


admin.site.site_header = "Niture Admin Panel"
admin.site.site_title = "Niture Admin Panel"
admin.site.index_title = "Welcome to Niture Control Panel!"


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    ordering = ('id',)
    list_display = (
        'id',
        'get_full_name',
        'first_name',
        'last_name',
        'username',
        'email',
        'image',
        'phone_number',
        'gender',
        'birthday',
        'get_age',
        'is_staff',
        'is_superuser',
        'is_active',
        'last_login',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'is_active',
        'is_staff',
        'is_superuser',
        'gender',
    )
    search_fields = (
        'first_name',
        'last_name',
        'email',
        'username',
    )
    readonly_fields = (
        'id',
        'get_age',
        'created_at',
        'updated_at',
        'last_login',
        "date_joined",
    )

    fieldsets = (
        (None, {
            'fields': ('username', 'email', 'password',)
        }),
        ('Personal Info', {
            'fields': ('first_name', 'last_name', 'description', 'phone_number', 'image', 'gender',)
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser')
        }),
        ('Important Dates', {
        'fields': ('created_at', 'updated_at', "date_joined", 'last_login', 'birthday', 'get_age',)
        }),
    )

    add_fieldsets = (
        ('Create Super User', {
            'classes': ('wide',),
            'fields': ('username', 'email', 'first_name', 'last_name', 'phone_number', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser',)}
        ),
    )
