# Generated by Django 2.2.15 on 2020-08-24 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0013_sponsor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilephoto',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
