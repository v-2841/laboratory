# Generated by Django 4.2.4 on 2023-08-23 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reagents', '0003_reagentname_alter_reagent_options_alter_reagent_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reagentname',
            name='name',
            field=models.CharField(max_length=200, unique=True, verbose_name='Название реактива'),
        ),
    ]