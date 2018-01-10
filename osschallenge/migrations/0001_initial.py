# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-18 08:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_markdown.models
import easy_thumbnails.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', django_markdown.models.MarkdownField(max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('links', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=50)),
                ('key', models.CharField(max_length=10, unique=True)),
                ('picture', easy_thumbnails.fields.ThumbnailerImageField(null=True, upload_to=b'profile-pictures')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('title_en_us', models.CharField(max_length=50, null=True, verbose_name='Title')),
                ('title_de', models.CharField(max_length=50, null=True, verbose_name='Title')),
                ('lead_text', models.CharField(max_length=300, verbose_name='Lead text')),
                ('lead_text_en_us', models.CharField(max_length=300, null=True, verbose_name='Lead text')),
                ('lead_text_de', models.CharField(max_length=300, null=True, verbose_name='Lead text')),
                ('description', models.CharField(max_length=5000, verbose_name='Description')),
                ('description_en_us', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_de', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('licence', models.CharField(max_length=50, verbose_name='Licence')),
                ('website', models.CharField(max_length=50, verbose_name='Website')),
                ('github', models.CharField(max_length=50)),
                ('active', models.BooleanField(default=True)),
                ('mentors', models.ManyToManyField(related_name='project_mentors', to=settings.AUTH_USER_MODEL, verbose_name='Mentors')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_owner', to=settings.AUTH_USER_MODEL, verbose_name='Owner')),
            ],
        ),
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('required_points', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('title_en_us', models.CharField(max_length=50, null=True, verbose_name='Title')),
                ('title_de', models.CharField(max_length=50, null=True, verbose_name='Title')),
                ('lead_text', models.CharField(max_length=300, verbose_name='Lead text')),
                ('lead_text_en_us', models.CharField(max_length=300, null=True, verbose_name='Lead text')),
                ('lead_text_de', models.CharField(max_length=300, null=True, verbose_name='Lead text')),
                ('description', models.CharField(max_length=5000, verbose_name='Description')),
                ('description_en_us', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_de', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('task_done', models.BooleanField(default=False)),
                ('task_checked', models.BooleanField(default=False)),
                ('picture', easy_thumbnails.fields.ThumbnailerImageField(null=True, upload_to=b'')),
                ('approval_date', models.DateField(null=True)),
                ('approved_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('assignee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assignee_tasks', to=settings.AUTH_USER_MODEL, verbose_name='Assignee')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='osschallenge.Project')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='rank',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='osschallenge.Rank'),
        ),
        migrations.AddField(
            model_name='profile',
            name='role',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='osschallenge.Role'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='osschallenge.Task'),
        ),
    ]
