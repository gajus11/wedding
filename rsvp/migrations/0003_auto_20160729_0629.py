# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-29 06:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0002_auto_20160720_0834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rsvp',
            name='adults_number',
            field=models.PositiveIntegerField(verbose_name='dorośli'),
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='childrens_number',
            field=models.PositiveIntegerField(verbose_name='dzieci'),
        ),
    ]