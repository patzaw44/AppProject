# Generated by Django 4.0 on 2021-12-28 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carsapp', '0006_rate_car_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='rating',
            field=models.DecimalField(decimal_places=1, max_digits=3, null=True),
        ),
    ]
