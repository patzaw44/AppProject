# Generated by Django 4.0 on 2021-12-28 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carsapp', '0013_alter_car_avg_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='rates_number',
            field=models.SmallIntegerField(default=0),
        ),
    ]
