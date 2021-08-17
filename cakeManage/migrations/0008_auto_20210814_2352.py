# Generated by Django 3.2.6 on 2021-08-14 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cakeManage', '0007_store_lat'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='lon',
            field=models.CharField(default=125.3, max_length=20, verbose_name='경도'),
        ),
        migrations.AlterField(
            model_name='store',
            name='lat',
            field=models.CharField(default=37.2, max_length=20, verbose_name='위도'),
        ),
    ]