# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-22 13:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entities', '0050_event_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='video',
            field=models.URLField(blank=True),
        ),
    ]
