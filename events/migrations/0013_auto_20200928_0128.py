# Generated by Django 2.2.16 on 2020-09-27 23:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_event_sponsors'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventparticipant',
            old_name='show',
            new_name='event',
        ),
    ]
