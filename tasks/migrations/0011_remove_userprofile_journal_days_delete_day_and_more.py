# Generated by Django 4.2.6 on 2024-02-14 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0010_day_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='journal_days',
        ),
        migrations.DeleteModel(
            name='Day',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='journal_days',
            field=models.CharField(default='Monday', max_length=10),
            preserve_default=False,
        ),
    ]