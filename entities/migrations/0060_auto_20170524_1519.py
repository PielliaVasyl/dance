# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-24 15:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entities', '0059_auto_20170524_1331'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopType',
            fields=[
                ('abstracttype_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='entities.AbstractType')),
                ('title', models.CharField(choices=[('INSH', 'Интернет-магазин'), ('ORSH', 'Магазин')], default='ORSH', max_length=4)),
            ],
            bases=('entities.abstracttype',),
        ),
        migrations.AlterField(
            model_name='placetype',
            name='title',
            field=models.CharField(choices=[('OADP', 'Open air')], default='OADP', max_length=4),
        ),
    ]
