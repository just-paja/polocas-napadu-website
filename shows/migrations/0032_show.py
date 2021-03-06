# Generated by Django 2.2.16 on 2020-09-20 00:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_event'),
        ('shows', '0031_delete_shows'),
    ]

    operations = [
        migrations.CreateModel(
            name='Show',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='events.Event')),
            ],
            options={
                'verbose_name': 'Show',
                'verbose_name_plural': 'Shows',
            },
            bases=('events.event',),
        ),
    ]
