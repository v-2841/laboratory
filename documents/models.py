from django.db import models


class Document(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='Название',
    )
    standard = models.CharField(
        max_length=32,
        blank=True,
        null=True,
        verbose_name='Нормативный документ',
    )
    file = models.FileField(
        upload_to='documents',
        verbose_name='Файл',
    )

    class Meta:
        ordering = ('-standard', 'name')
        verbose_name = 'Нормативный документ'
        verbose_name_plural = 'Нормативные документы'

    def __str__(self):
        if self.standard:
            return f'{self.standard} - {self.name}'
        return self.name
