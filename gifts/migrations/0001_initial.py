# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-20 12:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='nazwa')),
                ('image', models.ImageField(upload_to='', verbose_name='obrazek')),
                ('link', models.CharField(max_length=200, verbose_name='link')),
                ('is_reserved', models.BooleanField(default=False, verbose_name='zarezerwowane')),
                ('reserver', models.CharField(max_length=200, verbose_name='osoba_rezerwująca')),
            ],
        ),
    ]
