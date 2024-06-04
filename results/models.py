from django.db import models

from users.models import User


class Result(models.Model):
    sample_name = models.CharField(
        max_length=200,
        verbose_name='Название образца',
    )
    analysis_name = models.CharField(
        max_length=200,
        verbose_name='Название исследования',
    )
    standard = models.CharField(
        max_length=200,
        verbose_name='Нормативный документ',
    )
    measurement_unit = models.CharField(
        max_length=200,
        verbose_name='Единица измерения',
    )
    result = models.CharField(
        max_length=200,
        verbose_name='Результат исследования',
    )
    is_processed = models.BooleanField(
        default=False,
        verbose_name='Обработан',
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
    )
    researcher = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='results',
        verbose_name='Исследователь',
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Результат исследования'
        verbose_name_plural = 'Результаты исследований'

    def __str__(self):
        return (f'{self.pub_date.strftime("%d.%m.%Y")}'
                + f' - {self.sample_name} - {self.analysis_name}')
