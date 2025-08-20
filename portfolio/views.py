from django.shortcuts import render, get_object_or_404
from .models import Portfolio, PortfolioCategory


def portfolio_list(request):
    categories = PortfolioCategory.objects.filter(is_active=True)
    portfolios = Portfolio.objects.filter(is_active=True)
    return render(
        request,
        "portfolio/list.html",
        {"portfolios": portfolios, "categories": categories},
    )


def portfolio_detail(request, slug):
    portfolio = get_object_or_404(Portfolio, slug=slug, is_active=True)
    portfolio.views += 1
    portfolio.save()
    return render(request, "portfolio/detail.html", {"portfolio": portfolio})
