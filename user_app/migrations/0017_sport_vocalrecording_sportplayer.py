# Generated by Django 4.2.5 on 2023-12-28 07:47

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0016_alter_cashtransaction_transaction_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('players', models.PositiveIntegerField()),
                ('equipment', models.CharField(max_length=100)),
                ('images', models.ImageField(upload_to='Sport/Sport/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='VocalRecording',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('artist_profile', models.ImageField(upload_to='artist/artist_profile/%Y/%m/%d')),
                ('recording_date', models.DateField(default=datetime.datetime(2023, 12, 28, 7, 47, 44, 683469, tzinfo=datetime.timezone.utc))),
                ('audio_file', models.FileField(upload_to='artist/vocal_recordings/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='SportPlayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=50)),
                ('images', models.ImageField(upload_to='Sport/Sportplayer/%Y/%m/%d')),
                ('sport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_app.sport')),
            ],
        ),
    ]
