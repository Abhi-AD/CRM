# Generated by Django 4.2.5 on 2023-12-22 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0002_alter_billrecord_bill_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billrecord',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]