# Generated by Django 2.2.dev20190104142447 on 2019-01-12 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("locations", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="location",
            options={"verbose_name": "Location", "verbose_name_plural": "Locations"},
        ),
    ]
