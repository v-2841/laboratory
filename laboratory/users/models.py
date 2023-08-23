from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

from users.validators import validate_username


class User(AbstractUser):
    username = models.CharField(
        max_length=settings.USER_PROFILE_LENGHT,
        blank=False,
        unique=True,
        verbose_name='Ник',
        validators=[validate_username],
        error_messages={
            'unique': 'Пользователь с таким ником уже существует',
        },
    )
    first_name = models.CharField(
        max_length=settings.USER_PROFILE_LENGHT,
        blank=False,
        verbose_name='Имя',
    )
    last_name = models.CharField(
        max_length=settings.USER_PROFILE_LENGHT,
        blank=False,
        verbose_name='Фамилия',
    )

    class Meta:
        ordering = ('last_name', 'first_name',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
