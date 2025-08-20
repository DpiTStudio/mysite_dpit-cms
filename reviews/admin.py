from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "phone", "is_moderated", "created_at")
    list_editable = ("is_moderated",)
    list_filter = ("is_moderated", "created_at")
    search_fields = ("full_name", "email", "phone", "message")
    readonly_fields = ("created_at",)
    date_hierarchy = "created_at"

    fieldsets = (
        ("Информация о клиенте", {"fields": ("full_name", "phone", "email")}),
        ("Отзыв", {"fields": ("message",)}),
        ("Модерация", {"fields": ("is_moderated", "created_at")}),
    )

    actions = ["approve_reviews", "disapprove_reviews"]

    def approve_reviews(self, request, queryset):
        queryset.update(is_moderated=True)
        self.message_user(request, f"{queryset.count()} отзывов одобрено")

    approve_reviews.short_description = "Одобрить выбранные отзывы"

    def disapprove_reviews(self, request, queryset):
        queryset.update(is_moderated=False)
        self.message_user(request, f"{queryset.count()} отзывов отклонено")

    disapprove_reviews.short_description = "Отклонить выбранные отзывы"
