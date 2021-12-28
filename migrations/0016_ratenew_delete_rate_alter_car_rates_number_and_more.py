# Generated by Django 4.0 on 2021-12-28 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carsapp', '0015_alter_car_rates_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='RateNew',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_id', models.SmallIntegerField()),
                ('rating', models.IntegerField(default=5, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Rate',
        ),
        migrations.AlterField(
            model_name='car',
            name='rates_number',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ratenew',
            name='car_rate_data',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carsapp.car'),
        ),
    ]
