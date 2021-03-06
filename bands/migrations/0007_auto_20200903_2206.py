# Generated by Django 2.2.16 on 2020-09-03 20:06

from django.db import migrations
import images.fields


class Migration(migrations.Migration):

    dependencies = [
        ('bands', '0006_auto_20200824_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='logo',
            field=images.fields.ImageField(blank=True, help_text='imageHelpText', null=True, upload_to='bands', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='bandphoto',
            name='image',
            field=images.fields.ImageField(height_field='height', help_text='imageHelpText', upload_to='var/photos', verbose_name='Image', width_field='width'),
        ),
    ]
