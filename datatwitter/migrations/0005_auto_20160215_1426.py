# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-15 14:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datatwitter', '0004_auto_20160215_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twitter',
            name='tweet',
            field=models.ForeignKey(default='00', on_delete=django.db.models.deletion.CASCADE, to='datatwitter.Tweet'),
        ),
    ]
