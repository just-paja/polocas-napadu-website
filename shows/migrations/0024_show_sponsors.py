# Generated by Django 2.2.13 on 2020-08-04 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0013_sponsor'),
        ('shows', '0023_auto_20200308_2243'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='sponsors',
            field=models.ManyToManyField(to='profiles.Sponsor'),
        ),
    ]
