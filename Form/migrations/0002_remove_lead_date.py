# Generated by Django 3.0.7 on 2020-06-27 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Form', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lead',
            name='date',
        ),
    ]