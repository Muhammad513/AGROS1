# Generated by Django 4.1.6 on 2023-02-09 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0007_alter_paxta_kond_alter_paxta_xisobi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paxta',
            name='ifloslik',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='paxta',
            name='namlik',
            field=models.FloatField(),
        ),
    ]