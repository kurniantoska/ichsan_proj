# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 15:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_auto_20170829_2125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mahasiswa',
            name='fakultas_dan_program_studi',
        ),
        migrations.AddField(
            model_name='mahasiswa',
            name='program_studi',
            field=models.CharField(choices=[('Ekonomi', (('ak', 'Akuntansi'), ('man', 'Manajemen'))), ('Teknik', (('ar', 'Arsitektur'), ('el', 'Elektro')))], default='ak', max_length=30),
            preserve_default=False,
        ),
    ]
