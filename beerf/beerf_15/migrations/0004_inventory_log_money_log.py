# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-13 18:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beerf_15', '0003_inventory,retailer added'),
    ]

    operations = [
        migrations.CreateModel(
            name='inventory_log',
            fields=[
                ('ilid', models.AutoField(primary_key=True, serialize=False)),
                ('turn', models.IntegerField()),
                ('change', models.IntegerField()),
                ('ifid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beerf_15.factories')),
            ],
        ),
        migrations.CreateModel(
            name='money_log',
            fields=[
                ('mlid', models.AutoField(primary_key=True, serialize=False)),
                ('turn', models.IntegerField()),
                ('change', models.IntegerField()),
                ('mfid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beerf_15.factories')),
            ],
        ),
    ]
