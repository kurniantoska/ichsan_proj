from django.db import models
from django.conf import settings
from base.models import Penelitian, Mahasiswa, Dosen
from django.core.urlresolvers import reverse
from .utils import write_roman

User = settings.AUTH_USER_MODEL

# Create your models here.
class SuratIzinPenelitianMahasiswa(models.Model):
    created             = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated             = models.DateTimeField(auto_now=True, null=True, blank=True)
    disetujui           = models.BooleanField(default=False)
    penelitian          = models.OneToOneField(Penelitian)

    def get_created_month_roman(self):
        bulan = self.created.month
        return write_roman(bulan)

    def get_objects_mahasiswa(self):
        return self.penelitian.mahasiswa.all()

    def get_penelitian_judul(self):
        return self.penelitian.judul

    def get_absolute_url(self):
        return reverse('lemlit:detail-surat-penelitian-mahasiswa', kwargs={'pk' : self.id})

    def get_absolute_url_cetak_pdf(self):
        return reverse('lemlit:cetak-surat-penelitian-mahasiswa', kwargs={'pk' : self.id})

    def __str__(self):
        return "{} - {}".format(self.penelitian.mahasiswa.first(), self.penelitian.judul)

class StrukturManajemen(models.Model):
    nama_dosen          = models.ForeignKey(Dosen)
    jabatan             = models.CharField(max_length=30)

    def __str__(self):
        return self.nama_dosen.nama

class PetugasAdmininistrasi(models.Model):
    user                = models.ForeignKey(User)
    def __str__(self):
        return self.user.first_name



