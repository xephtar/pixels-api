# Generated by Django 4.0.3 on 2022-04-13 19:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canvas', '0003_alter_canvasdata_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Check',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.TextField(unique=True)),
                ('end_time', models.DateTimeField(default=datetime.datetime(2022, 4, 13, 19, 16, 33, 512998))),
            ],
        ),
    ]
