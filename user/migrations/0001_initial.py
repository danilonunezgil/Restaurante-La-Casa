# Generated by Django 3.1.1 on 2021-11-04 22:28

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
            name='person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cc', models.IntegerField(default=0)),
                ('names', models.CharField(max_length=150)),
                ('last_names', models.CharField(max_length=150)),
                ('celphone', models.IntegerField(default=0)),
                ('address', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('rol', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='profil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=150)),
                ('active', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('id_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.person')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
