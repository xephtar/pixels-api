# Generated by Django 4.0.3 on 2022-04-17 22:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('canvas', '0006_alter_check_end_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 17, 22, 7, 38, 678177, tzinfo=utc)),
        ),
    ]
