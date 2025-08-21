from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import NewsCategory, News
from ckeditor_uploader.widgets import CKEditorUploadingWidget


@admin.register(NewsCategory)
class NewsCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "logo_preview", "order", "is_active", "news_count")
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

    def news_count(self, obj):
        return obj.news_set.count()

    news_count.short_description = "Кол-во новостей"


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = (
        "idimage_preview",
        "title",
        "category",
        "is_active",
        "created_at",
        "views",
    )
    list_editable = ("is_active",)
    list_filter = ("category", "is_active", "created_at")
    search_fields = ("title", "seo_title", "seo_description")
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ("image_preview", "created_at", "updated_at")
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
