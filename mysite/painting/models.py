from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

"""
class Users(models.Model):
    id_user = models.AutoField("id", primary_key=True)
    FIO = models.CharField("ФИО", max_length=100)
    login = models.CharField("Логин", max_length=50)
    password = models.CharField("Пароль", max_length=100)
    user_img = models.ImageField("Изображение", upload_to="users/")

    def __str__(self):
        return self.FIO

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
"""


class Reviews(models.Model):
    id_rev = models.AutoField(primary_key=True)
    name = models.CharField("Имя", max_length=50)
    reviews = models.TextField("Комментарий", max_length=1000)

    def __str__(self):
        return 'Comment by {}'.format(self.name)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"


class Pictures(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    title = models.TextField()
    img = models.ImageField(upload_to="images/")
    liked = models.ManyToManyField(User, default=None, blank=True, related_name='liked')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    @property
    def num_likes(self):
        return self.liked.all().count()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"


LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Pictures, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)

    def __str__(self):
        return str(self.post)


class Lessons(models.Model):
    title = models.CharField(max_length=100)
    info = models.TextField()
    image = models.ImageField(upload_to="lessons/")
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def pub(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
