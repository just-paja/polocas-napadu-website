# Generated by Django 2.2.15 on 2020-08-24 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200305_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapterphoto',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]