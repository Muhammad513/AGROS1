# Generated by Django 4.1.6 on 2023-02-06 17:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brigada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('br_num', models.IntegerField()),
                ('br_full_name', models.CharField(max_length=200)),
                ('G_gektar', models.FloatField()),
                ('P_gektar', models.FloatField()),
                ('G_reja', models.FloatField()),
                ('P_reja', models.FloatField()),
                ('mavsum', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Hudud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('h_num', models.IntegerField()),
                ('Agranom_full_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Massiv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Maxsulot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Punkt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='XarajatTuri',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='XarajatRejasi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brlik', models.TextField(choices=[('????', '????'), ('????????', '????????'), ('??????????', '??????????'), ('????????????????', '????????????????')], max_length=30)),
                ('kolvo', models.IntegerField()),
                ('summa', models.IntegerField()),
                ('brigada', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Home.brigada')),
                ('maxsulot', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Home.maxsulot')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.xarajatturi')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('pic', models.ImageField(blank=True, null=True, upload_to='img')),
                ('friends', models.ManyToManyField(related_name='my_friend', to='Home.friend')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Paxta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('sofVazn', models.IntegerField()),
                ('ifloslik', models.IntegerField()),
                ('namlik', models.IntegerField()),
                ('xisobi', models.IntegerField(blank=True)),
                ('kond', models.IntegerField(blank=True)),
                ('brigada', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Home.brigada')),
                ('punkt', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Home.punkt')),
            ],
        ),
        migrations.AddField(
            model_name='friend',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Home.profile'),
        ),
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=1000)),
                ('seen', models.BooleanField(default=False)),
                ('msg_receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='msg_receiver', to='Home.profile')),
                ('msg_sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='msg_sender', to='Home.profile')),
            ],
        ),
        migrations.AddField(
            model_name='brigada',
            name='hudud',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Home.hudud'),
        ),
        migrations.AddField(
            model_name='brigada',
            name='massiv',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.massiv'),
        ),
    ]
