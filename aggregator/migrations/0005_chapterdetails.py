# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-05 05:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aggregator', '0004_content_contenttitle'),
    ]

    operations = [
        migrations.CreateModel(
            name='chapterDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapterDescription', models.TextField(max_length=10000)),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aggregator.content')),
            ],
        ),
    ]
