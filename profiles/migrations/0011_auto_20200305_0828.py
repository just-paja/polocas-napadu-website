# Generated by Django 2.2.10 on 2020-03-05 08:28

from django.db import migrations
import fields.weight


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0010_auto_20191029_0832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilegroup',
            name='weight',
            field=fields.weight.WeightField(default=False, help_text='weightHelpText', verbose_name='Weight'),
        ),
    ]
