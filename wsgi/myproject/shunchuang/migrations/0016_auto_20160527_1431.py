# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-27 14:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shunchuang', '0015_auto_20160527_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='which_class',
            field=models.CharField(blank=True, choices=[('\u7ba1\u7406\u7c7b', '\u7ba1\u7406\u7c7b'), ('\u8ba1\u7b97\u673a\u7c7b', '\u8ba1\u7b97\u673a\u7c7b'), ('\u673a\u68b0\u7c7b', '\u673a\u68b0\u7c7b'), ('\u5916\u8bed\u7c7b', '\u5916\u8bed\u7c7b'), ('\u4e2d\u6587\u7c7b', '\u4e2d\u6587\u7c7b'), ('\u5efa\u7b51\u7c7b', '\u5efa\u7b51\u7c7b'), ('\u827a\u672f\u7c7b', '\u827a\u672f\u7c7b'), ('\u7269\u7535\u7c7b', '\u7269\u7535\u7c7b'), ('\u6570\u5b66\u7c7b', '\u6570\u5b66\u7c7b'), ('\u6750\u6599\u7c7b', '\u6750\u6599\u7c7b'), ('\u6587\u65c5\u7c7b', '\u6587\u65c5\u7c7b'), ('\u751f\u5de5\u7c7b', '\u751f\u5de5\u7c7b')], max_length=20),
        ),
    ]
