from django.db import models
from django.contrib.auth.models import AbstractUser

from .validators import validate_username


class User(AbstractUser):
    """Модель пользователя."""

    username = models.CharField(
        'Имя пользователя',
        unique=True,
        max_length=150,
        validators=(validate_username,)
    )
    email = models.EmailField('Электронная почта', unique=True)
    # first_name = models.CharField(
    #     verbose_name='Имя',
    #     max_length=150
    # )
    # last_name = models.CharField(
    #     verbose_name='Фамилия',
    #     max_length=150
    # )
    bio = models.TextField('Биография', blank=True)
    avatar = models.ImageField(
        'Аватар',
        upload_to='users_avatars/',
        blank=True,
        null=True
    )
    confirmation_code = models.TextField('Код подтверждения', blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('date_joined',)

    def __str__(self):
        return self.username

    @property
    def is_admin(self):
        return self.is_superuser or self.role == 'admin'

    @property
    def is_moderator(self):
        return self.role == 'moderator'
