# Generated by Django 2.2.6 on 2020-01-23 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_auto_20200123_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='datafile',
            name='indexed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dataset',
            name='indexed',
            field=models.BooleanField(default=False),
        ),
    ]