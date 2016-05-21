# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-21 09:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shunchuang', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=11)),
                ('email', models.CharField(max_length=30)),
                ('select', models.BooleanField()),
                ('age', models.IntegerField()),
                ('motto', models.CharField(blank=True, max_length=100)),
                ('find', models.CharField(blank=True, max_length=200)),
                ('hibby', models.CharField(blank=True, max_length=50)),
                ('city', models.CharField(blank=True, max_length=20)),
                ('school', models.CharField(blank=True, max_length=20)),
                ('school_class', models.CharField(blank=True, max_length=20)),
                ('which_class', models.CharField(blank=True, max_length=20)),
                ('person_photo', models.CharField(blank=True, max_length=30)),
            ],
        ),
    ]
