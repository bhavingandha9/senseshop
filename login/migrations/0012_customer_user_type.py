# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-01-05 07:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0011_auto_20180104_1335'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='user_type',
            field=models.CharField(default='user', max_length=10),
        ),
    ]
