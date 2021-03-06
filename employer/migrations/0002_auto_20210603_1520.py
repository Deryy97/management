# Generated by Django 3.2.4 on 2021-06-03 13:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employer',
            name='age',
        ),
        migrations.AddField(
            model_name='employer',
            name='address',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='employer',
            name='birthday',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='employer',
            name='birthplace',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='employer',
            name='company_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='employer',
            name='education',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='employer',
            name='father_name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='employer',
            name='id_card',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='employer',
            name='hire_date',
            field=models.DateField(),
        ),
    ]
