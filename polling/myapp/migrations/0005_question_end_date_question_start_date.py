# Generated by Django 5.0.4 on 2024-05-07 18:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='End Date'),
        ),
        migrations.AddField(
            model_name='question',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Start Date'),
        ),
    ]