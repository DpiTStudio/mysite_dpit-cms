from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import News, NewsCategory


def news_list(request):
    categories = NewsCategory.objects.filter(is_active=True)
    news_list = News.objects.filter(is_active=True).select_related("category")

    # Пагинация - 9 новостей на страницу (3 ряда по 3)
    paginator = Paginator(news_list, 9)
    page_number = request.GET.get("page")
    news = paginator.get_page(page_number)

    return render(request, "news/list.html", {"news": news, "categories": categories})


def news_detail(request, slug):
    news_item = get_object_or_404(News, slug=slug, is_active=True)
    news_item.views += 1
    news_item.save()
    return render(request, "news/detail.html", {"news_item": news_item})
