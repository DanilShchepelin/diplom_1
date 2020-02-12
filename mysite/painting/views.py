from django.shortcuts import render
from django.views.generic.base import View

from .models import Reviews


class ReviewsView(View):
    def get(self, request):
        review = Reviews.objects.all()
        return render(request, "reviews/reviews_list.html", {"reviews_list": review})
