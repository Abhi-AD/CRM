# Generated by Django 4.2.5 on 2023-12-26 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0003_staff_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selling_price', models.PositiveIntegerField()),
                ('cost_price', models.PositiveIntegerField()),
                ('quantity', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=100)),
                ('using_date', models.IntegerField()),
            ],
        ),
    ]
