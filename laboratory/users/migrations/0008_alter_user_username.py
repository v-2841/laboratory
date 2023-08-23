# Generated by Django 4.2.4 on 2023-08-23 08:06

from django.db import migrations, models
import users.validators


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'unique': 'Пользователь с таким ником уже существует'}, max_length=200, unique=True, validators=[users.validators.validate_username], verbose_name='Ник'),
        ),
    ]