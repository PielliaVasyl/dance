# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-08 16:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entities', '0022_auto_20170508_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='socials',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='entities.Socials'),
        ),
    ]
