# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-02-25 16:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0013_auto_20180224_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='au_id',
            field=models.DecimalField(decimal_places=0, max_digits=20, unique=True),
        ),
    ]