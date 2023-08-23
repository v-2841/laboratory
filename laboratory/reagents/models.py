from django.db import models


GRADES = [
    ('тех.', 'Технический'),
    ('ч.', 'Чистый'),
    ('ч.д.а.', 'Чистый для анализа'),
    ('х.ч.', 'Химически чистый'),
    ('сп.ч.', 'Спектрально чистый'),
    ('осч', 'Особо чистый'),
]


class ReagentName(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True,
        verbose_name='Название реактива',
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Название реактива'
        verbose_name_plural = 'Названия реактивов'

    def __str__(self):
        return self.name


class Reagent(models.Model):
    index = models.PositiveSmallIntegerField(
        unique=True,
        verbose_name='Индекс',
    )
    name = models.ForeignKey(
        ReagentName,
        on_delete=models.CASCADE,
        verbose_name='Название реактива',
    )
    grade = models.CharField(
        max_length=10,
        choices=GRADES,
        blank=True,
        verbose_name='Марка',
    )
    expiration_date = models.DateField(
        verbose_name='Годен до',
    )

    class Meta:
        ordering = ('index',)
        verbose_name = 'Реактив'
        verbose_name_plural = 'Реактивы'

    def __str__(self):
        return self.name.name
