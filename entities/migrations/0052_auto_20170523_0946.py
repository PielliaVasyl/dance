# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-23 09:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entities', '0051_event_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='danceclass',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='danceclass',
            name='video',
            field=models.URLField(blank=True),
        ),
    ]