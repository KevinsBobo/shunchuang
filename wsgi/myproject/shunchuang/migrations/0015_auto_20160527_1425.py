# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-27 14:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shunchuang', '0014_auto_20160527_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='which_class',
            field=models.CharField(blank=True, choices=[(b'management', '\u7ba1\u7406\u7c7b'), (b'computer', '\u8ba1\u7b97\u673a\u7c7b'), (b'mechanic', '\u673a\u68b0\u7c7b'), (b'language', '\u5916\u8bed\u7c7b'), (b'chinese', '\u4e2d\u6587\u7c7b'), (b'architechure', '\u5efa\u7b51\u7c7b'), (b'art', '\u827a\u672f\u7c7b'), (b'electrical', '\u7269\u7535\u7c7b'), (b'math', '\u6570\u5b66\u7c7b'), (b'material', '\u6750\u6599\u7c7b'), (b'tour', '\u6587\u65c5\u7c7b'), (b'sangon', '\u751f\u5de5\u7c7b')], max_length=20),
        ),
    ]
