# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-31 16:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aggregator', '0002_auto_20170531_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='longDescription',
            field=models.TextField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='content',
            name='shortDescription',
            field=models.TextField(max_length=10000),
        ),
    ]
