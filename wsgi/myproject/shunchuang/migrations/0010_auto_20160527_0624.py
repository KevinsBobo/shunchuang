# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-27 06:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shunchuang', '0009_auto_20160527_0512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='select',
            field=models.IntegerField(choices=[(b'chuangye', 1), (b'zudui', 2)]),
        ),
    ]
