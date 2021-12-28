# Generated by Django 4.0 on 2021-12-28 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carsapp', '0010_alter_rate_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='car_id',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='rate',
            name='rating',
            field=models.DecimalField(decimal_places=1, max_digits=3, null=True),
        ),
    ]
