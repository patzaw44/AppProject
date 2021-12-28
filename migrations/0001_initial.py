# Generated by Django 4.0 on 2021-12-26 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=44)),
                ('model', models.CharField(max_length=44)),
                ('avg_rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('rates_number', models.IntegerField()),
            ],
        ),
    ]