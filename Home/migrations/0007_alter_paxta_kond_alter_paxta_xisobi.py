# Generated by Django 4.1.6 on 2023-02-09 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0006_galla_tr_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paxta',
            name='kond',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='paxta',
            name='xisobi',
            field=models.FloatField(blank=True),
        ),
    ]
