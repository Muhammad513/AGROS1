# Generated by Django 4.1.7 on 2023-02-14 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0020_maxsulot_narxnoma_ishxaqqi'),
    ]

    operations = [
        migrations.AddField(
            model_name='ishxaqqi',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='ishxaqqi',
            name='summa',
            field=models.FloatField(blank=True),
        ),
    ]
