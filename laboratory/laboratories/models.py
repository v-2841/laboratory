from django.db import models
from django.core.exceptions import ValidationError


class Laboratory(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True,
        verbose_name='Название лаборатории',
    )
    description = models.TextField(
        verbose_name='Описание',
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Лаборатория'
        verbose_name_plural = 'Лаборатории'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.pk and Laboratory.objects.exists():
            raise ValidationError('Нельзя создать более одной лаборатории')
        return super(Laboratory, self).save(*args, **kwargs)

    def delete(self):
        raise ValidationError('Нельзя удалить лабораторию')
