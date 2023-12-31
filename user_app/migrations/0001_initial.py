# Generated by Django 4.2.5 on 2023-12-22 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BillRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_number', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('description', models.TextField()),
                ('item_name', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('customer_name', models.CharField(max_length=100)),
                ('payment_status', models.CharField(choices=[('pending', 'Pending'), ('paid', 'Paid')], max_length=20)),
            ],
        ),
    ]
