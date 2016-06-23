# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-23 11:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0009_auto_20160622_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='affiliation',
            name='avatar',
            field=models.FileField(blank=True, null=True, upload_to='uploads/avatars/'),
        ),
        migrations.AlterField(
            model_name='individual',
            name='avatar',
            field=models.FileField(blank=True, null=True, upload_to='uploads/avatars/'),
        ),
    ]
