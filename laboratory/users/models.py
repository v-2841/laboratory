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
    )
    email = models.EmailField(
        blank=False,
        unique=True,
        verbose_name='Электронная почта',
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
    laboratory_staff = models.BooleanField(
        default=False,
        verbose_name='Администратор лаборатории',
        help_text='Указывает, что пользователь '
                  + 'является администратором лаборатории',
    )

    class Meta:
        ordering = ('username',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Invitation(models.Model):
    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Отправитель',
    )
    email = models.EmailField(
        blank=False,
        verbose_name='Электронная почта',
    )
    token = models.CharField(
        max_length=100,
        blank=False,
        verbose_name='Токен',
    )
    is_used = models.BooleanField(
        default=False,
        verbose_name='Использован',
    )

    class Meta:
        ordering = ('email',)
        verbose_name = 'Приглашение'
        verbose_name_plural = 'Приглашения'

    def __str__(self):
        return self.sender.username + ' to ' + self.email
