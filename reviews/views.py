from django.shortcuts import render, redirect
from .models import Review
from django.contrib import messages


def reviews_list(request):
    reviews = Review.objects.filter(is_moderated=True)
    return render(request, "reviews/list.html", {"reviews": reviews})


def add_review(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        message = request.POST.get("message")

        Review.objects.create(
            full_name=full_name, phone=phone, email=email, message=message
        )
        messages.success(request, "Ваш отзыв отправлен на модерацию!")
        return redirect("reviews_list")

    return render(request, "reviews/add.html")
