from django.db import models


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


class Reviews(models.Model):
    id_rev = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(Users, on_delete=models.CASCADE)
    reviews = models.TextField("Комментарий", max_length=1000)

    def __str__(self):
        return self.reviews

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"


class Images(models.Model):
    id_img = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(Users, on_delete=models.CASCADE)
    description = models.TextField("Описание")
    img = models.ImageField("Изображение", upload_to="images/")

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"
