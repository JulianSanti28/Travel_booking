# Generated by Django 3.2.4 on 2021-10-12 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travel_booking', '0003_auto_20211012_1021'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserved',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reserved',
            name='flight',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='reservas_vuelo', to='travel_booking.flight'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reserved',
            name='price',
            field=models.FloatField(default=None),
            preserve_default=False,
        ),
    ]