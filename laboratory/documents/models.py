from django.db import models


class Document(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True,
        verbose_name='Название',
    )
    file = models.FileField(
        upload_to='documents',
        verbose_name='Файл',
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Нормативный документ'
        verbose_name_plural = 'Нормативные документы'

    def __str__(self):
        return self.name
