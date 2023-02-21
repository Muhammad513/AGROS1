# Generated by Django 4.1.6 on 2023-02-08 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_lavozim_profile_lavozim'),
    ]

    operations = [
        migrations.CreateModel(
            name='OmborG',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Galla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('sofVazn', models.IntegerField()),
                ('yuk_num', models.CharField(max_length=3)),
                ('tr_marka', models.CharField(choices=[('ЗИЛ', 'ЗИЛ'), ('КАМАЗ', 'КАМАЗ'), ('БОШКА', 'БОШКА')], max_length=20)),
                ('tr_num', models.CharField(max_length=20)),
                ('brigada', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Home.brigada')),
                ('ombor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.omborg')),
            ],
        ),
    ]
