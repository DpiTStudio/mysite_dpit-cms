from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import PortfolioCategory, Portfolio


@admin.register(PortfolioCategory)
class PortfolioCategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "slug",
        "logo_preview",
        "order",
        "is_active",
        "portfolio_count",
    )
    list_editable = ("order", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    readonly_fields = ("logo_preview",)

    def logo_preview(self, obj):
        if obj.logo:
            return mark_safe(
                f'<img src="{obj.logo.url}" width="50" height="50" style="object-fit: cover;" />'
            )
        return "Нет изображения"

    logo_preview.short_description = "Логотип"

    def portfolio_count(self, obj):
        return obj.portfolio_set.count()

    portfolio_count.short_description = "Кол-во работ"


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category",
        "image_preview",
        "price",
        "can_order",
        "views",
        "is_active",
    )
    list_editable = ("price", "can_order", "is_active")
    list_filter = ("category", "can_order", "is_active", "created_at")
    search_fields = ("title", "seo_title")
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ("views", "image_preview", "created_at", "updated_at")
    date_hierarchy = "created_at"

    fieldsets = (
        (
            "Основная информация",
            {
                "fields": (
                    "category",
                    "title",
                    "slug",
                    "image",
                    "image_preview",
                    "content",
                )
            },
        ),
        ("Цена и заказы", {"fields": ("price", "can_order")}),
        (
            "SEO информация",
            {"fields": ("seo_title", "seo_keywords", "seo_description")},
        ),
        ("Статистика", {"fields": ("views", "created_at", "updated_at")}),
        ("Статус", {"fields": ("is_active",)}),
    )

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(
                f'<img src="{obj.image.url}" width="50" height="50" style="object-fit: cover;" />'
            )
        return "Нет изображения"

    image_preview.short_description = "Изображение"
