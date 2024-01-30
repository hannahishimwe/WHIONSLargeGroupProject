# Generated by Django 4.2.6 on 2024-01-27 16:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=30, unique=True, validators=[django.core.validators.RegexValidator(message='Username must consist of at least three alphanumericals', regex='\\w{3,}$')]),
        ),
    ]