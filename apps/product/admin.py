from django.contrib import admin

from .models import Category, Banner, Product, Review


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ordering = ('id',)
    readonly_fields = ('id', 'created_at', 'updated_at',)
    list_display = (
        'id',
        'name',
        'image',
        'is_active',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'name',
    )
    list_filter = (
        'is_active',
        'name',
    )


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    ordering = ('-id',)
    readonly_fields = ('id', 'created_at', 'updated_at',)
    list_display = (
        'id',
        'name',
        'image',
        'is_active',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'name',
    )
    list_filter = (
        'is_active',
        'name',
    )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    ordering = ('id',)
    readonly_fields = ('id', 'created_at', 'updated_at',)
    list_display = (
        'id',
        'user__email',
        'product',
        'product__category',
        'user',
        'rate',
        'is_active',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'user__username',
        'user__first_name',
        'user__last_name',
        'user__email',
        'product__name',
        'product__category__name',
    )
    list_filter = (
        'is_active',
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    ordering = ('name',)
    readonly_fields = ('id', 'created_at', 'updated_at',)
    prepopulated_fields = {
        'slug': ('name',),
    }
    list_display = (
        'id',
        'name',
        'image',
        'price',
        'percentage',
        'category',
        'views',
        'discount',
        'reviews_count',
        'is_active',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'name',
        'category',
    )
    list_filter = (
        'is_active',
    )
