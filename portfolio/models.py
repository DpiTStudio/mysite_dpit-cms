from django.db import models


class PortfolioCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    slug = models.SlugField(unique=True, verbose_name="URL")
    content = models.TextField(verbose_name="Описание", blank=True, null=True)
    logo = models.ImageField(upload_to="portfolio/categories/", verbose_name="Логотип")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок")
    is_active = models.BooleanField(default=True, verbose_name="Активно")

    class Meta:
        verbose_name = "Категория портфолио"
        verbose_name_plural = "Категории портфолио"
        ordering = ["order"]

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    category = models.ForeignKey(
        PortfolioCategory, on_delete=models.CASCADE, verbose_name="Категория"
    )
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    slug = models.SlugField(unique=True, verbose_name="URL")
    image = models.ImageField(upload_to="portfolio/images/", verbose_name="Изображение")
    seo_title = models.CharField(max_length=200, verbose_name="SEO Заголовок")
    seo_keywords = models.CharField(max_length=200, verbose_name="SEO Ключевые слова")
    seo_description = models.CharField(max_length=255, verbose_name="SEO Описание")
    content = models.TextField(verbose_name="Описание", blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    can_order = models.BooleanField(default=True, verbose_name="Можно заказать")
    views = models.PositiveIntegerField(default=0, verbose_name="Просмотры")
    is_active = models.BooleanField(default=True, verbose_name="Активно")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Портфолио"
        verbose_name_plural = "Портфолио"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
