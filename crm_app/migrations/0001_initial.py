# Generated by Django 4.2.5 on 2023-12-25 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('position', models.CharField(choices=[('staff', 'satff'), ('manager', 'Manager'), ('Boss', 'Boss')], max_length=20)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('contact', models.CharField(max_length=10)),
                ('date_of_birth', models.DateField()),
                ('address', models.CharField(blank=True, max_length=255)),
                ('hire_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
