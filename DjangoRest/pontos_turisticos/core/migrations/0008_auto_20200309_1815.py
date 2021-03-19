# Generated by Django 3.0.4 on 2020-03-09 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
        ('core', '0007_auto_20200309_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='touristspot',
            name='location',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='locations.Location'),
        ),
    ]