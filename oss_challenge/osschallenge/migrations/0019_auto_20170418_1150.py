# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-18 09:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('osschallenge', '0018_task_task_checked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='picture',
            name='project',
        ),
        migrations.AddField(
            model_name='picture',
            name='task',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='osschallenge.Task'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='picture',
            name='picture',
            field=models.ImageField(default=b'osschallenge/pictures/no-img.jpg', upload_to=b'osschallenge/pictures/'),
        ),
    ]