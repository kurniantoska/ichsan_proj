# Generated by Django 2.1.5 on 2019-02-23 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lemlit', '0022_auto_20190123_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suratizinpenelitianmahasiswa',
            name='tujuan_surat',
            field=models.CharField(max_length=150),
        ),
    ]
