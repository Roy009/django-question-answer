# Generated by Django 3.2.12 on 2024-05-07 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='pub_date',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
    ]
