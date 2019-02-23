from django.conf import settings
from django.db import models
# from django.core.urlresolvers import reverse
from django.urls import reverse
from base.utils import get_program_studi_full_name
from utils import FAKULTAS_N_PRODI_CHOICES


class Mahasiswa(models.Model):
    nama = models.CharField(max_length=120)
    nim = models.CharField(unique=True, max_length=15)
    program_studi = models.CharField(max_length=30, choices=FAKULTAS_N_PRODI_CHOICES)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return '{} - {}'.format(self.nim, self.nama)

    def get_nama(self):
        return self.nama

    def get_absolute_url(self):
        return reverse('base:detail-mahasiswa', kwargs={'pk': self.id})

    def get_absolute_url_update(self):
        return reverse('base:update-mahasiswa', kwargs={'pk': self.id})

    def get_fakultas(self):
        d = dict(self.FAKULTAS_N_PRODI_CHOICES)
        for k, v in d.items():
            v = dict(v)
            for k1, v1 in v.items():
                if self.program_studi == k1:
                    return k
            if self.program_studi == k:
                return k

    def get_program_studi_name(self):
        return get_program_studi_full_name(self.program_studi)

    def save(self, *args, **kwargs):
        self.nim = self.nim.upper()
        self.nama = self.nama.title()
        super(Mahasiswa, self).save()

    class Meta:
        ordering = ['nim']


class Dosen(models.Model):
    gelar_depan = models.CharField(max_length=20, null=True, blank=True)
    nama_lengkap = models.CharField(max_length=120, null=True, blank=True)
    gelar_belakang = models.CharField(max_length=20)
    nidn = models.CharField(max_length=20, default='0123', unique=True)
    email = models.EmailField(null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    program_studi = models.CharField(choices=FAKULTAS_N_PRODI_CHOICES, max_length=30, blank=True, null=True)

    def get_fakultas(self):
        d = dict(FAKULTAS_N_PRODI_CHOICES)
        for k, v in d.items():
            v = dict(v)
            for k1, v1 in v.items():
                if self.program_studi == k1:
                    return k
            if self.program_studi == k:
                return k

    def __str__(self):
        return self.nidn + self.nama_lengkap


class Penelitian(models.Model):
    dosen = models.ManyToManyField(Dosen, blank=True)
    mahasiswa = models.ManyToManyField(Mahasiswa, blank=True)
    judul = models.CharField(unique=True, max_length=200)
    lokasi = models.CharField(max_length=120, null=True, blank=True)
    berkas_publikasi = models.FileField(upload_to='publikasi', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('base:detail-penelitian', kwargs={'pk': self.id})

    def get_absolute_url_update(self):
        return reverse('base:update-penelitian', kwargs={'pk': self.id})

    def get_all_mhs_in_penelitian(self):
        return self.mahasiswa.all()

    def __str__(self):
        return self.judul

    def save(self, *args, **kwargs):
        self.judul = self.judul.lower()
        super(Penelitian, self).save()
