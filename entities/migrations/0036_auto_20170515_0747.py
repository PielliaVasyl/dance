# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-15 07:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entities', '0035_audiowiki_song_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='audiowiki',
            old_name='song_author',
            new_name='singer',
        ),
    ]