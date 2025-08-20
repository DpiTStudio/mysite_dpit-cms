from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import AboutPage


@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    list_display = ("title", "image_preview", "is_active")
    list_editable = ("is_active",)
    readonly_fields = ("image_preview",)

    fieldsets = (
        (
            "Основная информация",
            {"fields": ("title", "content", "image", "image_preview")},
        ),
        (
            "SEO информация",
            {"fields": ("seo_title", "seo_keywords", "seo_description")},
        ),
        ("Статус", {"fields": ("is_active",)}),
    )

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(
                f'<img src="{obj.image.url}" width="50" height="50" style="object-fit: cover;" />'
            )
        return "Нет изображения"

    image_preview.short_description = "Изображение"
