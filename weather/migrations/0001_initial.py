# Generated by Django 3.2.7 on 2024-10-26 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CityWeather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=100)),
                ('temperature', models.FloatField()),
                ('weather_description', models.CharField(max_length=100)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]