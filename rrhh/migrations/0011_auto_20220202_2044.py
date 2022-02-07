# Generated by Django 3.1.1 on 2022-02-02 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rrhh', '0010_auto_20220202_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='recruitment',
            name='approvalsComments',
            field=models.CharField(blank=True, help_text='Enter the comments', max_length=500, verbose_name='Comments'),
        ),
        migrations.AddField(
            model_name='recruitment',
            name='requisitionApproved',
            field=models.BooleanField(default=False, help_text='Requisition Approved?', verbose_name='Requisition approved'),
        ),
        migrations.AlterField(
            model_name='recruitment',
            name='comments',
            field=models.CharField(blank=True, help_text='Enter the comments', max_length=500, verbose_name='Comments'),
        ),
    ]
