# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-08 15:48
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entities', '0020_remove_placeinmap_show_in_map_section'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=16, validators=[django.core.validators.RegexValidator(message="Введите номер телефона в формате: '+380XXXXXXX'. Разрешено до 15 цифр.", regex='^\\+?1?\\d{9,15}$')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entities.UserProfile')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.RemoveField(
            model_name='contacts',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='contacts',
            name='phone_numbers',
            field=models.ManyToManyField(blank=True, to='entities.PhoneNumber'),
        ),
    ]