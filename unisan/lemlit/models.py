from django.db import models
from django.conf import settings
from base.models import Penelitian, Mahasiswa, Dosen
from django.core.urlresolvers import reverse
from .utils import write_roman
from base.utils import get_fakultas_full_name, get_program_studi_full_name

User = settings.AUTH_USER_MODEL

# Create your models here.
class SuratIzinPenelitianMahasiswa(models.Model):
    nomor_surat         = models.CharField(unique=True, max_length=50)
    mahasiswa           = models.ForeignKey(Mahasiswa, null=True, blank=True)
    penelitian          = models.ForeignKey(Penelitian)
    nama_instansi       = models.CharField(max_length=80)
    tujuan_surat        = models.CharField(max_length=20)
    created             = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated             = models.DateTimeField(auto_now=True, null=True, blank=True)
    disetujui           = models.BooleanField(default=False)
    distempel           = models.BooleanField(default=False)


    def get_created_month_roman(self):
        bulan = self.created.month
        return write_roman(bulan)

    def get_absolute_url(self):
        return reverse('lemlit:detail-surat-penelitian-mahasiswa', kwargs={'pk' : self.id})

    def get_absolute_url_update(self):
        return reverse('lemlit:edit-surat-penelitian-mahasiswa', kwargs={'pk' : self.id})

    def get_absolute_url_cetak_pdf(self):
        return reverse('lemlit:cetak-surat-penelitian-mahasiswa', kwargs={'pk' : self.id})

    def get_fakultas(self):
        return get_fakultas_full_name(self.mahasiswa.program_studi)

    def get_program_studi_name(self):
        return get_program_studi_full_name(self.mahasiswa.program_studi)

    def get_ketua_lemlit_name(self):
        return StrukturManajemen.objects.get(jabatan='Ketua Lembaga Penelitian')


    def __str__(self):
        return self.penelitian.judul

class StrukturManajemen(models.Model):
    nama_dosen          = models.ForeignKey(Dosen)
    jabatan             = models.CharField(max_length=30)

    def __str__(self):
        return self.nama_dosen.nama

class PetugasAdmininistrasi(models.Model):
    user                = models.ForeignKey(User)
    def __str__(self):
        return self.user.first_name



