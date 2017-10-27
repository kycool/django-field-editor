# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-26 07:37
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=50, verbose_name='name')),
                ('extend', django.contrib.postgres.fields.jsonb.JSONField(default={}, verbose_name='extend data')),
            ],
        ),
    ]
