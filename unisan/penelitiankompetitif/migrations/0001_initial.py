# Generated by Django 2.1.5 on 2019-02-23 02:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0023_auto_20190123_0957'),
    ]

    operations = [
        migrations.CreateModel(
            name='PenelitianKompetitif',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periode', models.CharField(choices=[('genap', 'Genap'), ('gasal', 'Gasal')], max_length=5)),
                ('tahun', models.CharField(default=2019, max_length=4)),
                ('berkas_proposal', models.FileField(upload_to='penelitian_kompetitif')),
                ('berkas_laporan', models.FileField(upload_to='penelitian_kompetitif')),
                ('berkas_publikasi', models.FileField(upload_to='penelitian_kompetitif')),
                ('Dosen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nama_dosen', to='base.Dosen')),
                ('Penelitian', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='penelitian_dosen_kompetitif', to='base.Penelitian')),
            ],
        ),
    ]
