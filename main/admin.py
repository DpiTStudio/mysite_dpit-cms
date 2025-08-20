from django.contrib import admin
from .models import SiteMetadata


@admin.register(SiteMetadata)
class SiteMetadataAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "email", "phone", "is_active")
    list_editable = ("is_active",)
    list_filter = ("is_active",)
    search_fields = ("title", "author", "email")
    fieldsets = (
        ("Основная информация", {"fields": ("title", "description", "author")}),
        ("Контакты", {"fields": ("phone", "email", "address")}),
        ("SEO", {"fields": ("keywords",)}),
        ("Статус", {"fields": ("is_active",)}),
    )
