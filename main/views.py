from django.shortcuts import render
from .models import SiteMetadata


def home(request):
    metadata = SiteMetadata.objects.filter(is_active=True).first()
    return render(request, "main/home.html", {"metadata": metadata})
