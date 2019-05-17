# Generated by Django 2.2 on 2019-05-15 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('theatre_sports', '0016_auto_20190515_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scorepointpoll',
            name='winner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='winning_polls', to='theatre_sports.ScorePointPollVoting', verbose_name='Winner'),
        ),
    ]