# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 11:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lemlit', '0004_auto_20170824_1327'),
    ]

    operations = [
        migrations.AddField(
            model_name='suratizinpenelitianmahasiswa',
            name='disetujui',
            field=models.BooleanField(default=False),
        ),
    ]
