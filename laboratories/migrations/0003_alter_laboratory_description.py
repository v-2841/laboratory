# Generated by Django 4.2.4 on 2023-08-29 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratories', '0002_laboratory_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laboratory',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
    ]