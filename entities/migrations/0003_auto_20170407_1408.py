# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-07 14:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entities', '0002_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_link',
            field=models.URLField(blank=True),
        ),
    ]
