# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-24 08:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('osschallenge', '0010_auto_20171129_1551.py'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='rank',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='osschallenge.Rank'),
        ),
    ]
