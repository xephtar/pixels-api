# Generated by Django 4.0.3 on 2022-04-17 22:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('canvas', '0008_alter_check_end_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check',
            name='end_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
