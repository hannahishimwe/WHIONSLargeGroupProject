# Generated by Django 4.2.6 on 2024-03-27 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_template_permanently_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='template',
            name='unlock_after_days',
            field=models.IntegerField(default=0),
        ),
    ]