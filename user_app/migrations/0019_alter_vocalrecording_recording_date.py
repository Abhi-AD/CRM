# Generated by Django 4.2.5 on 2023-12-28 10:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0018_alter_vocalrecording_recording_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vocalrecording',
            name='recording_date',
            field=models.DateField(default=datetime.datetime(2023, 12, 28, 10, 32, 23, 609749, tzinfo=datetime.timezone.utc)),
        ),
    ]
