# Generated by Django 3.2.4 on 2021-06-02 15:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('age', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('hire_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]