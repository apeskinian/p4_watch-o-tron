# Generated by Django 5.1.1 on 2024-10-22 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watches', '0002_alter_watchlist_list_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='friendly_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='list_name',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]