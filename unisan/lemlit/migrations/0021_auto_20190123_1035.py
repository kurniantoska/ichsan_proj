# Generated by Django 2.1.5 on 2019-01-23 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lemlit', '0020_auto_20190123_0928'),
    ]

    operations = [
        migrations.AddField(
            model_name='pengumuman',
            name='tipe_pengummuman',
            field=models.CharField(choices=[('penelitian_hibah_internal', 'Hibah Penelitian Internal')], default='-', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pengumuman',
            name='berkas',
            field=models.FileField(blank=True, upload_to='pengumuman'),
        ),
    ]
