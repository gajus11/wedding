# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-19 10:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('when', models.DateTimeField()),
                ('where', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='')),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='SliderImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('text', models.CharField(max_length=200)),
                ('slider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wedding_app.Slider')),
            ],
        ),
        migrations.CreateModel(
            name='Wedding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('when', models.DateTimeField()),
                ('where', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='')),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
    ]