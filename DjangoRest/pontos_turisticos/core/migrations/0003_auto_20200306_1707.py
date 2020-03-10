# Generated by Django 3.0.4 on 2020-03-06 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attractions', '0001_initial'),
        ('perks', '0001_initial'),
        ('core', '0002_auto_20200306_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='touristspot',
            name='attractions',
            field=models.ManyToManyField(to='attractions.Attraction'),
        ),
        migrations.AddField(
            model_name='touristspot',
            name='perks',
            field=models.ManyToManyField(to='perks.Perk'),
        ),
    ]
