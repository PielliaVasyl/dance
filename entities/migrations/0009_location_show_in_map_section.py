# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-04 17:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entities', '0008_auto_20170504_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='show_in_map_section',
            field=models.BooleanField(default=False),
        ),
    ]