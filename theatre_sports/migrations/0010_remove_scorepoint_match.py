# Generated by Django 2.1.5 on 2019-02-04 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theatre_sports', '0009_auto_20190204_1918'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scorepoint',
            name='match',
        ),
    ]
