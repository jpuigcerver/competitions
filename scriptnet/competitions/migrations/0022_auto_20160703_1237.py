# -*- coding: utf-8 -*-
# Generated by Django 1.10.dev20160115151452 on 2016-07-03 09:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0021_subtrack_pertrack_uniqueid'),
    ]

    operations = [
        migrations.CreateModel(
            name='EvaluatorFunction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.SlugField(default='')),
            ],
        ),
        migrations.AddField(
            model_name='benchmark',
            name='evaluator_function_argumentordinal',
            field=models.IntegerField(default='1'),
        ),
        migrations.AlterField(
            model_name='benchmark',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='benchmark',
            name='evaluator_function',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='competitions.EvaluatorFunction'),
        ),
    ]
