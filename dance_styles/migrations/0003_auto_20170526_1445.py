# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-26 14:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dance_styles', '0002_dancestyleinsectionattendeeage_dancestyleinsectionaverageprice_dancestyleinsectionbetweenpartnersdis'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AveragePrice',
        ),
        migrations.DeleteModel(
            name='BetweenPartnersDistance',
        ),
        migrations.DeleteModel(
            name='CountType',
        ),
    ]
