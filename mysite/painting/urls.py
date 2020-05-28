from django.urls import path, include
from django.conf.urls import url
from . import views
from .views import register_user, like_post


urlpatterns = [
    path("", views.MainForm.as_view(), name="main"),
    path("reviews/", views.AddReviews.as_view(), name="add_review"),
    path("accounts/", include('django.contrib.auth.urls')),
    path("registration/", register_user, name="registration"),
    path("pictures/", views.post_list, name='post_list'),
    path('pictures/new/', views.post_new, name='post_new'),
    path('pictures/like/', like_post, name='post_like'),
    path('lessons/', views.lessons_list, name='lessons_list'),
    path('lessons/<int:pk>/', views.lessons_detail, name='lessons_detail'),
    path('search/', views.Search.as_view(), name='lessons_search'),
    path('test/', views.test, name='test'),
]