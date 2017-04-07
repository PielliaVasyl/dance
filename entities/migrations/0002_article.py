# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-07 14:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('is_linked_article', models.BooleanField(default=False)),
                ('article_link', models.ImageField(blank=True, upload_to='')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entities.UserProfile')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
