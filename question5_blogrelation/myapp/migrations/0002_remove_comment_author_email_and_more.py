# Generated by Django 5.0.4 on 2024-05-07 13:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='author_email',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='author_name',
        ),
        migrations.AddField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
