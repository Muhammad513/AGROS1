# Generated by Django 4.1.7 on 2023-02-14 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0014_xar_turi_delete_maxsulot_remove_xarajat_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='xarajat',
            name='turi',
        ),
        migrations.DeleteModel(
            name='Xar_turi',
        ),
    ]
