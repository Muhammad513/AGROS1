# Generated by Django 4.1.7 on 2023-02-14 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0021_ishxaqqi_date_alter_ishxaqqi_summa'),
    ]

    operations = [
        migrations.AddField(
            model_name='lavozim',
            name='bolim',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.CreateModel(
            name='Xodimlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('bolim', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Home.lavozim')),
            ],
        ),
        migrations.AddField(
            model_name='ishxaqqi',
            name='xodimlar',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Home.xodimlar'),
        ),
    ]
