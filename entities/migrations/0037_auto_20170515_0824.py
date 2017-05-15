# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-15 08:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entities', '0036_auto_20170515_0747'),
    ]

    operations = [
        migrations.CreateModel(
            name='AbstractWikiGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='AudioWikiPlaylistLink',
            fields=[
                ('abstractlink_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='entities.AbstractLink')),
            ],
            bases=('entities.abstractlink',),
        ),
        migrations.CreateModel(
            name='PhotoWiki',
            fields=[
                ('abstractwiki_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='entities.AbstractWiki')),
                ('photographer', models.CharField(blank=True, max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='')),
            ],
            bases=('entities.abstractwiki',),
        ),
        migrations.CreateModel(
            name='PhotoWikiTag',
            fields=[
                ('abstracttag_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='entities.AbstractTag')),
            ],
            bases=('entities.abstracttag',),
        ),
        migrations.CreateModel(
            name='VideoWikiPlaylistLink',
            fields=[
                ('abstractlink_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='entities.AbstractLink')),
            ],
            bases=('entities.abstractlink',),
        ),
        migrations.CreateModel(
            name='AudioWikiPlaylist',
            fields=[
                ('abstractwikigroup_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='entities.AbstractWikiGroup')),
                ('audios', models.ManyToManyField(blank=True, to='entities.AudioWiki')),
                ('dance_style', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entities.DanceStyle')),
                ('link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entities.AudioWikiPlaylistLink')),
            ],
            bases=('entities.abstractwikigroup',),
        ),
        migrations.CreateModel(
            name='VideoWikiPlaylist',
            fields=[
                ('abstractwikigroup_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='entities.AbstractWikiGroup')),
                ('dance_style', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entities.DanceStyle')),
                ('link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entities.VideoWikiPlaylistLink')),
                ('videos', models.ManyToManyField(blank=True, to='entities.VideoWiki')),
            ],
            bases=('entities.abstractwikigroup',),
        ),
        migrations.AddField(
            model_name='photowiki',
            name='tags',
            field=models.ManyToManyField(blank=True, to='entities.PhotoWikiTag'),
        ),
        migrations.AddField(
            model_name='abstractwikigroup',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entities.UserProfile'),
        ),
    ]