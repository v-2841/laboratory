# Generated by Django 4.2.4 on 2023-08-23 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_user_laboratory_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Электронная почта'),
        ),
        migrations.DeleteModel(
            name='Invitation',
        ),
    ]
