from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    image = models.ImageField(upload_to='user_image', blank=True, null=True, verbose_name="Аватар")

    class Meta:
        db_table = 'user'
        verbose_name = " Пользователи"
        verbose_name_plural = "Ползователи"

    def __str__(self):
        return self.name
    