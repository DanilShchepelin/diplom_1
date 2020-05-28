from django.views.generic import ListView, TemplateView
from django.db.models import Q

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from .models import Reviews, Pictures, Lessons, Like
from .forms import ReviewsForm, SignUpForm, PictureForm
from django.utils import timezone


class MainForm(View):
    def get(self, request):
        reviews = Reviews.objects.all()
        return render(request, "main/index.html", {"reviews": reviews})


class AddReviews(View):
    def post(self, request):
        form = ReviewsForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")


def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            return redirect("/accounts/login")
    else:
        form = SignUpForm()
    return render(request, "registration/reg.html", {"form": form})


def post_list(request):
    pictures = Pictures.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, "main/post_list.html", {'pictures': pictures})


def post_new(request):
    if request.method == "POST":
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            picture = form.save(commit=False)
            picture.user = request.user
            picture.published_date = timezone.now()
            picture.save()
            return redirect('/pictures/')
    else:
        form = PictureForm()
    return render(request, "main/post_edit.html", {'form': form})


def lessons_list(request):
    lessons = Lessons.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, "lessons/lessons_search.html", {'lessons': lessons})


def lessons_detail(request, pk):
    lesson = get_object_or_404(Lessons, pk=pk)
    return render(request, 'lessons/lessons_detail.html', {'lesson': lesson})


class Search(ListView):
    model = Lessons
    template_name = 'lessons/lessons_list.html'

    def get_queryset(self):
        queryset = Lessons.objects.all()
        q = self.request.GET.get('q')
        if q:
            return queryset.filter(Q(title__icontains=q))

        return queryset


def like_post(request):
    user = request.user
    if request.method == "POST":
        post_id = request.POST.get('post_id')
        post_obj = Pictures.objects.get(id=post_id)

        if user in post_obj.liked.all():
            post_obj.liked.remove(user)
        else:
            post_obj.liked.add(user)
        """
        like, created = Like.objects.get_or_create(user, post_id=post_id)

        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'
        """
        post_obj.save()
    #return redirect('post_list')
    return HttpResponseRedirect('/pictures')


def test(request):
    return render(request, 'test/test.html', {})