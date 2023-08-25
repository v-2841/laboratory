from django.db import models


GRADES = [
    ('тех.', 'Технический'),
    ('ч.', 'Чистый'),
    ('ч.д.а.', 'Чистый для анализа'),
    ('х.ч.', 'Химически чистый'),
    ('сп.ч.', 'Спектрально чистый'),
    ('осч', 'Особо чистый'),
]


class Reagent(models.Model):
    index = models.PositiveSmallIntegerField(
        unique=True,
        null=True,
        verbose_name='Индекс',
    )
    name = models.CharField(
        max_length=200,
        unique=True,
        verbose_name='Название реактива',
    )
    grade = models.CharField(
        max_length=10,
        choices=GRADES,
        null=True,
        verbose_name='Марка',
    )
    expiration_date = models.DateField(
        verbose_name='Годен до',
        null=True,
    )

    class Meta:
        ordering = ('index',)
        verbose_name = 'Реактив'
        verbose_name_plural = 'Реактивы'

    def __str__(self):
        return self.name
