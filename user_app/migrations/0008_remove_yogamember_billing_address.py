# Generated by Django 4.2.5 on 2023-12-24 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0007_yogamember_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='yogamember',
            name='billing_address',
        ),
    ]
