from django.db import models
from django.conf import settings
# from django.core.urlresolvers import reverse
from django.urls import reverse
from base.models import Penelitian, Mahasiswa, Dosen


from .utils import write_roman
from base.utils import get_program_studi_full_name

from base.static_var import (
    TAHUN_AKADEMIK, STS_PN_HBH
)

User = settings.AUTH_USER_MODEL


class SuratIzinPenelitianMahasiswa(models.Model):

    KWITANSI_OPTION = (
        ('Surat Keterangan', 'Surat Keterangan'),
        ('Surat Izin Penelitian', 'Surat Izin Penelitian')
    )

    nomor_surat = models.CharField(max_length=50)
    mahasiswa = models.ForeignKey(Mahasiswa, null=True, blank=True, on_delete=models.CASCADE)
    penelitian = models.ForeignKey(Penelitian, on_delete=models.CASCADE)
    nama_instansi = models.CharField(max_length=80)
    tujuan_surat = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    disetujui = models.BooleanField(default=False)
    distempel = models.BooleanField(default=False)
    petugas = models.CharField(max_length=50, null=True, blank=True)
    untuk_pembayaran = models.CharField(max_length=25, choices=KWITANSI_OPTION, default='Surat Izin Penelitian')

    def get_created_month_roman(self):
        bulan = self.created.month
        return write_roman(bulan)

    def get_absolute_url(self):
        return reverse('lemlit:detail-surat-penelitian-mahasiswa', kwargs={'pk': self.id})

    def get_absolute_url_update(self):
        return reverse('lemlit:edit-surat-penelitian-mahasiswa', kwargs={'pk': self.id})

    def get_absolute_url_delete(self):
        return reverse('lemlit:delete-surat-penelitian-mahasiswa', kwargs={'pk': self.id})

    def get_absolute_url_cetak_surat_izin(self):
        return reverse('lemlit:cetak-surat-izin-penelitian-mahasiswa', kwargs={'pk': self.id})

    def get_absolute_url_cetak_kwitansi_izin(self):
        return reverse('lemlit:cetak-kwitansi-surat-izin-penelitian-mahasiswa', kwargs={'pk': self.id})

    def get_absolute_url_cetak_surat_keterangan(self):
        return reverse('lemlit:cetak-surat-keterangan-penelitian-mahasiswa', kwargs={'pk': self.id})

    def get_fakultas(self):
        return self.mahasiswa.get_fakultas()

    def get_program_studi_name(self):
        return get_program_studi_full_name(self.mahasiswa.program_studi)

    def get_ketua_lemlit_name(self):
        return StrukturManajemen.objects.get(jabatan='Ketua Lembaga Penelitian')

    def __str__(self):
        return self.penelitian.judul

    class Meta:
        ordering = ['created', 'updated']


class SuratKeteranganPenelitianMahasiswa(SuratIzinPenelitianMahasiswa):
    def __str__(self):
        return self.penelitian.judul


class StrukturManajemen(models.Model):
    nama_dosen = models.ForeignKey(Dosen, on_delete=models.CASCADE)
    jabatan = models.CharField(max_length=30)

    def __str__(self):
        return self.nama_dosen.nama


class PetugasAdmininistrasi(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name


class Status(models.Model):
    timestamp = models.DateTimeField()
    progress = models.CharField(choices=STS_PN_HBH, max_length=10)


class HibahPenelitian(models.Model):
    tahun = models.CharField(max_length=4)
    periode = models.CharField(choices=TAHUN_AKADEMIK, max_length=5)
    berkas_proposal = models.FileField()
    laporan_akhir = models.FileField()
    update = models.ForeignKey(Status, related_name='hibah_penelitian', on_delete=models.CASCADE)
    penelitian = models.ForeignKey(Penelitian, related_name='hibah_penelitian_internal', on_delete=models.CASCADE)
    dosen = models.CharField(max_length=55, blank=True, null=True)
    program_studi = models.CharField(max_length=30, blank=True, null=True)


class Pengumuman(models.Model):
    ANN_TYPE = (
        ('penelitian_hibah_internal', 'Hibah Penelitian Internal'),
    )
    tanggal = models.DateTimeField(auto_now_add=True)
    judul = models.CharField(max_length=30)
    deskripsi = models.TextField()
    berkas = models.FileField(blank=True, upload_to='pengumuman')
    tipe_pengummuman = models.CharField(choices=ANN_TYPE, max_length=30)
    tahun = models.CharField(max_length=4)
    periode = models.CharField(choices=TAHUN_AKADEMIK, max_length=5)
