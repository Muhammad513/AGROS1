# Generated by Django 4.1.6 on 2023-02-06 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_alter_friend_profile_alter_profile_friends_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='friends',
            field=models.ManyToManyField(blank=True, related_name='my_friend', to='Home.friend'),
        ),
    ]
