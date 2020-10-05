# Generated by Django 2.2.16 on 2020-09-20 01:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_update_content_types'),
        ('shows', '0034_auto_20200920_0249'),
        ('theatre_sports', '0023_retarget_shows'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='show',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='match', to='shows.Show'),
        ),
    ]