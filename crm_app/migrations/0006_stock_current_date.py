# Generated by Django 4.2.5 on 2023-12-27 05:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0005_stock_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='current_date',
            field=models.DateField(default=datetime.datetime(2023, 12, 27, 5, 12, 14, 757378, tzinfo=datetime.timezone.utc), verbose_name=datetime.datetime(2023, 12, 27, 5, 12, 7, 724540, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
