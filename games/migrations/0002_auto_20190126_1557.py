# Generated by Django 3.0.dev20190119234541 on 2019-01-26 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("games", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="game",
            name="rules",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="games",
                to="games.GameRules",
            ),
        ),
        migrations.AlterField(
            model_name="game",
            name="show",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="games",
                to="shows.Show",
            ),
        ),
        migrations.AlterField(
            model_name="gameinspiration",
            name="game",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="game_inspirations",
                to="games.Game",
            ),
        ),
        migrations.AlterField(
            model_name="gameinspiration",
            name="inspiration",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="inspiration_games",
                to="inspirations.Inspiration",
            ),
        ),
        migrations.AlterField(
            model_name="gamerules", name="description", field=models.TextField(),
        ),
    ]
