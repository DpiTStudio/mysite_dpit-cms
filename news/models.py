from django.db import models
from ckeditor.fields import RichTextField


class NewsCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    slug = models.SlugField(unique=True, verbose_name="URL")
    logo = models.ImageField(upload_to="news/categories/", verbose_name="Логотип")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок")
    is_active = models.BooleanField(default=True, verbose_name="Активно")

    class Meta:
        verbose_name = "Категория новостей"
        verbose_name_plural = "Категории новостей"
        ordering = ["order"]

    def __str__(self):
        return self.name


class News(models.Model):
    category = models.ForeignKey(
        NewsCategory, on_delete=models.CASCADE, verbose_name="Категория"
    )
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    slug = models.SlugField(unique=True, verbose_name="URL")
    image = models.ImageField(upload_to="news/images/", verbose_name="Изображение")
    seo_title = models.CharField(max_length=200, verbose_name="SEO Заголовок")
    seo_keywords = models.CharField(max_length=200, verbose_name="SEO Ключевые слова")
    seo_description = models.CharField(max_length=255, verbose_name="SEO Описание")
    content_short = models.CharField(
        max_length=255, verbose_name="Красткое  описание", blank=True, null=True
    )
    content = models.TextField(verbose_name="Основное оописание", blank=True, null=True)
    # content = RichTextField(verbose_name="Содержание")
    # content_short = RichTextField(verbose_name="Краткое содержание")
    # content = RichTextField(verbose_name="Содержание")
    views = models.PositiveIntegerField(default=0, verbose_name="Просмотры")
    is_active = models.BooleanField(default=True, verbose_name="Активно")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
