# Generated by Django 2.2.10 on 2020-03-05 10:54

from django.db import migrations
import fields.weight


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200305_0828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='weight',
            field=fields.weight.WeightField(default=100, help_text='weightHelpText', verbose_name='Weight'),
        ),
        migrations.AlterField(
            model_name='poem',
            name='weight',
            field=fields.weight.WeightField(default=100, help_text='weightHelpText', verbose_name='Weight'),
        ),
    ]
