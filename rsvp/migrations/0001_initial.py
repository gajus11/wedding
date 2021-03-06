# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-19 10:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RSVP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='imię')),
                ('last_name', models.CharField(max_length=100, verbose_name='nazwisko')),
                ('adults_number', models.PositiveIntegerField(default=1, verbose_name='dorośli')),
                ('children_number', models.PositiveIntegerField(default=0, verbose_name='dzieci')),
                ('transport', models.BooleanField(default=False, verbose_name='transport')),
                ('accomodation', models.BooleanField(default=False, verbose_name='nocleg')),
            ],
        ),
    ]
