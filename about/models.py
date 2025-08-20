from django.db import models
from ckeditor.fields import RichTextField


class AboutPage(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = RichTextField(verbose_name="Содержание")
    image = models.ImageField(upload_to="about/", verbose_name="Изображение")
    seo_title = models.CharField(max_length=200, verbose_name="SEO Заголовок")
    seo_keywords = models.CharField(max_length=200, verbose_name="SEO Ключевые слова")
    seo_description = models.CharField(max_length=255, verbose_name="SEO Описание")
    is_active = models.BooleanField(default=True, verbose_name="Активно")

    class Meta:
        verbose_name = "Страница о нас"
        verbose_name_plural = "Страницы о нас"

    def __str__(self):
        return self.title
