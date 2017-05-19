# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-19 11:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entities', '0042_auto_20170517_1313'),
    ]

    operations = [
        migrations.CreateModel(
            name='AbstractType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entities.UserProfile')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]