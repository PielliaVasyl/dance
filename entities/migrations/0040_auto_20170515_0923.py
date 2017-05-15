# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-15 09:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entities', '0039_auto_20170515_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiowiki',
            name='link',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='entities.AudioWikiLink'),
        ),
        migrations.AlterField(
            model_name='videowiki',
            name='link',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='entities.VideoWikiLink'),
        ),
    ]
