# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-02-18 16:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0002_auto_20180218_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='flag',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=2, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='flag',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=2, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='flag',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=2, null=True),
        ),
    ]
