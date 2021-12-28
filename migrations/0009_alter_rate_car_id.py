# Generated by Django 4.0 on 2021-12-28 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carsapp', '0008_alter_rate_car_id_alter_rate_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='car_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='rating', to='carsapp.car'),
        ),
    ]