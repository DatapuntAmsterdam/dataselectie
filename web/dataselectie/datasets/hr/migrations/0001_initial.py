# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-10 12:24
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataSelectie',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('bag_vbid', models.CharField(blank=True, db_index=True, max_length=16, null=True)),
                ('api_json', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
            options={
                'verbose_name_plural': 'Handelsregister dataselecties',
                'managed': True,
                'verbose_name': 'Handelsregister dataselectie',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='DummyTabel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('bla', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Dummy tabel',
                'managed': True,
                'verbose_name': 'Dummy tabel',
                'ordering': ('id',),
            },
        ),
    ]
