# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-05 18:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entities', '0004_auto_20170405_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='role',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
    ]