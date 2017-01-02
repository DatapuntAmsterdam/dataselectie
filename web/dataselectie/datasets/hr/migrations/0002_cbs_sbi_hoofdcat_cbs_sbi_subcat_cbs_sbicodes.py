# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-12 21:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CBS_sbi_hoofdcat',
            fields=[
                ('hcat', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('hoofdcategorie', models.CharField(max_length=140)),
            ],
            options={
                'ordering': ('hcat',),
                'verbose_name': 'Handelsregister sbi hoofdcategorie',
                'verbose_name_plural': 'Handelsregister sbi hoofdcategorieen',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CBS_sbi_subcat',
            fields=[
                ('scat', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('subcategorie', models.CharField(max_length=140)),
                ('hcat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.CBS_sbi_hoofdcat')),
            ],
            options={
                'ordering': ('scat',),
                'verbose_name': 'Handelsregister sbi subcategorie',
                'verbose_name_plural': 'Handelsregister sbi subcategorieen',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CBS_sbicodes',
            fields=[
                ('sbi_code', models.CharField(max_length=14, primary_key=True, serialize=False)),
                ('sub_sub_categorie', models.CharField(max_length=140)),
                ('scat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.CBS_sbi_subcat')),
            ],
        ),
    ]