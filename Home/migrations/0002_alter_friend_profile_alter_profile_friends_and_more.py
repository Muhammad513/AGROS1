# Generated by Django 4.1.6 on 2023-02-06 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='profile',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Home.profile'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='friends',
            field=models.ManyToManyField(null=True, related_name='my_friend', to='Home.friend'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pic',
            field=models.ImageField(blank=True, default='img/default.jpg', null=True, upload_to='img'),
        ),
    ]