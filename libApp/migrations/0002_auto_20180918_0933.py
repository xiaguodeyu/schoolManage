# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-18 01:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowbook',
            name='return_date',
            field=models.DateField(default=datetime.datetime(2018, 10, 18, 9, 33, 47, 510000)),
        ),
    ]