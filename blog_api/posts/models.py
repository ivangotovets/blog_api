from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Post(models.Model):
    MAX_POST_LEN = 16

    title = models.CharField(
        max_length=79,
        verbose_name='Название'
    )
    text = models.TextField(verbose_name='Текст поста')
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата изменения'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
    )

    class Meta:
        ordering = ('-created',)
        default_related_name = 'posts'
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.text[:self.MAX_POST_LEN]
