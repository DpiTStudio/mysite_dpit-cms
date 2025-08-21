from django.db import models


class SiteMetadata(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок сайта")
    description = models.CharField(max_length=200, verbose_name="Описание сайта")
    keywords = models.CharField(max_length=200, verbose_name="Ключевые слова")
    author = models.CharField(max_length=100, verbose_name="Автор")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Email")
    address = models.CharField(max_length=200, verbose_name="Адрес")
    is_active = models.BooleanField(default=True, verbose_name="Активно")

    class Meta:
        verbose_name = "Метаданные сайта"
        verbose_name_plural = "Метаданные сайта"

    def __str__(self):
        return self.title
