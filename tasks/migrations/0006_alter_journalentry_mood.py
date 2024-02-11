# Generated by Django 4.2.6 on 2024-02-10 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_alter_journalentry_mood'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journalentry',
            name='mood',
            field=models.IntegerField(choices=[(1, '😔'), (2, '🙁'), (3, '😐'), (4, '🙂'), (5, '😄')], default=3),
        ),
    ]