# Generated by Django 3.1.1 on 2022-02-02 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rrhh', '0008_auto_20220202_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruitment',
            name='jobDescription',
            field=models.ForeignKey(help_text='Select job description', null=True, on_delete=django.db.models.deletion.CASCADE, to='rrhh.jobdescription', verbose_name='Job description'),
        ),
    ]
