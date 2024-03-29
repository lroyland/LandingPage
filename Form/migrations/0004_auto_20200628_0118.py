# Generated by Django 3.0.7 on 2020-06-28 01:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Form', '0003_auto_20200627_2233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lead',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='lead',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='lead',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lead',
            name='modified',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
