# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-15 14:26
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datatwitter', '0003_files'),
    ]

    operations = [
        migrations.AddField(
            model_name='files',
            name='file_title',
            field=models.TextField(default='Untitled', max_length=100),
        ),
        migrations.AddField(
            model_name='twitter',
            name='tweet',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='datatwitter.Tweet'),
        ),
        migrations.AlterField(
            model_name='files',
            name='file_path',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location='/datatwitter/files/'), upload_to='%y%m%d/%f'),
        ),
    ]
