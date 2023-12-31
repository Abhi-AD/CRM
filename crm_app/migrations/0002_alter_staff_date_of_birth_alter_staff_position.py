# Generated by Django 4.2.5 on 2023-12-25 08:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='date_of_birth',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='staff',
            name='position',
            field=models.CharField(choices=[('staff', 'staff'), ('manager', 'Manager'), ('Boss', 'Boss')], max_length=20),
        ),
    ]
