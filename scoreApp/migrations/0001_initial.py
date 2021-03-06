# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-09-17 08:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('recordApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScoreInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_type', models.CharField(max_length=20)),
                ('exam_date', models.DateField()),
                ('score', models.PositiveIntegerField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recordApp.StuInfo')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recordApp.Subject')),
            ],
        ),
    ]
