# Generated by Django 2.1.5 on 2019-01-23 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lemlit', '0021_auto_20190123_1035'),
    ]

    operations = [
        migrations.AddField(
            model_name='pengumuman',
            name='periode',
            field=models.CharField(choices=[('gasal', 'Gasal'), ('genap', 'Genap')], default='gasal', max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pengumuman',
            name='tahun',
            field=models.CharField(default='2019', max_length=4),
            preserve_default=False,
        ),
    ]
