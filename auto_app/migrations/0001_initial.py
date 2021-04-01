# Generated by Django 3.1.7 on 2021-03-14 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brend', models.CharField(max_length=255)),
                ('car_model', models.CharField(max_length=255)),
                ('release_year', models.IntegerField()),
                ('gearbox', models.SmallIntegerField(choices=[(0, 'manual '), (1, 'automatic '), (2, 'robotic')], default=0)),
                ('body_color', models.CharField(max_length=255)),
            ],
        ),
    ]