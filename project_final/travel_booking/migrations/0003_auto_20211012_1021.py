# Generated by Django 3.2.4 on 2021-10-12 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel_booking', '0002_auto_20211012_1009'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='price',
            field=models.FloatField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='price',
            field=models.FloatField(default=None),
            preserve_default=False,
        ),
    ]
