# Generated by Django 5.1.1 on 2024-10-04 10:13

import cloudinary.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WatchList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='WatchMovement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movement_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Watch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=100)),
                ('collection', models.CharField(blank=True, max_length=100)),
                ('model', models.CharField(blank=True, max_length=100)),
                ('movement_model', models.CharField(blank=True, max_length=50)),
                ('image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('complication_chronograph', models.BooleanField(default=False)),
                ('complication_date', models.BooleanField(default=False)),
                ('complication_day', models.BooleanField(default=False)),
                ('complication_gmt', models.BooleanField(default=False)),
                ('complication_world_timer', models.BooleanField(default=False)),
                ('complication_moonphase', models.BooleanField(default=False)),
                ('complication_power_reserve', models.BooleanField(default=False)),
                ('complication_tourbillon', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watch_owner', to=settings.AUTH_USER_MODEL)),
                ('list_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watch_list', to='watches.watchlist')),
                ('movement_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watch_movement', to='watches.watchmovement')),
            ],
        ),
    ]