# Generated by Django 2.1.4 on 2018-12-08 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('gps', models.CharField(blank=True, max_length=127, null=True)),
                ('name', models.CharField(max_length=127)),
                ('website', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
