# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-25 15:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0011_auto_20160623_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='slug',
            field=models.SlugField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='submission',
            name='method_info',
            field=models.TextField(default=''),
        ),
    ]
