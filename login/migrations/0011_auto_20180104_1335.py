# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-01-04 08:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0010_auto_20171223_1714'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='flag',
            new_name='cflag',
        ),
    ]
