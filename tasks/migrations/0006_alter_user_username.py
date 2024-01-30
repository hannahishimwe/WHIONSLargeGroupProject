# Generated by Django 4.2.6 on 2024-01-30 11:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_user_preferred_days_to_journal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=30, unique=True, validators=[django.core.validators.RegexValidator(message='Username must consist of at least three alphanumericals', regex='^\\w{3,}$')]),
        ),
    ]