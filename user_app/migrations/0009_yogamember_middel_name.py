# Generated by Django 4.2.5 on 2023-12-24 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0008_remove_yogamember_billing_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='yogamember',
            name='middel_name',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
