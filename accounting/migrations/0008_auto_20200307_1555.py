# Generated by Django 2.2.11 on 2020-03-07 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0007_auto_20200305_1054'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bankscrape',
            options={'verbose_name': 'Bank Scrape', 'verbose_name_plural': 'Bank scrapes'},
        ),
        migrations.AlterModelOptions(
            name='debt',
            options={'verbose_name': 'Debt', 'verbose_name_plural': 'Debts'},
        ),
        migrations.AlterModelOptions(
            name='pricelevel',
            options={'verbose_name': 'Price level', 'verbose_name_plural': 'Price levels'},
        ),
        migrations.AlterModelOptions(
            name='purpose',
            options={'verbose_name': 'Purpose', 'verbose_name_plural': 'Purposes'},
        ),
        migrations.AlterModelOptions(
            name='statement',
            options={'verbose_name': 'Statement', 'verbose_name_plural': 'Statements'},
        ),
        migrations.AlterField(
            model_name='promise',
            name='repeat',
            field=models.CharField(blank=True, choices=[(None, 'Never'), ('P1M', 'Monthly'), ('P1Y', 'Yearly')], max_length=31, null=True, verbose_name='Repeat'),
        ),
    ]
