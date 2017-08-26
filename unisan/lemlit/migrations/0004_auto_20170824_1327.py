# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 05:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lemlit', '0003_remove_suratizinpenelitianmahasiswa_mahasiswa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='petugasadmininistrasi',
            name='email',
        ),
        migrations.RemoveField(
            model_name='petugasadmininistrasi',
            name='nama',
        ),
        migrations.AddField(
            model_name='petugasadmininistrasi',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
