# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-02-24 11:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0012_auto_20180223_2333'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='payments',
            new_name='payment',
        ),
    ]