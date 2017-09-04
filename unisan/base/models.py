
from django.db import models
from django.core.urlresolvers import reverse
from base.utils import get_program_studi_full_name

# Create your models here.

class Mahasiswa(models.Model):
    FAKULTAS_N_PRODI_CHOICES = (
        ('Fakultas Ekonomi', (
            ('ak', 'Akuntansi'),
            ('man', 'Manajemen'),
            )
        ),
        ('Fakultas Ilmu Komputer', (
            ('si', 'Sistem Informasi'),
            ('ti', 'Teknik Informatika'),
         )
         ),
        ('Fakultas Hukum', (
            ('pe', 'Perdata'),
            ('pi', 'Pidana'),
            ('za', 'TEST hukum')
         )
         ),
        ('Fakultas Teknik', (
            ('ar', 'Arsitektur'),
            ('el', 'Elektro'),
        )
        ),
        ('Fakultas Ilmu Sosial, Ilmu Politik', (
            ('ko', 'Komunikasi'),
            ('ad', 'Administrasi'),
        )
        ),
        ('Fakultas Pertanian', (
            ('ab', 'Agribisnis'),
            ('thp', 'Teknologi Hasil Pertanian'),
        )
        ),
    )

    nama                            = models.CharField(max_length=120)
    nim                             = models.CharField(unique=True, max_length=15)
    program_studi                   = models.CharField(max_length=30, choices=FAKULTAS_N_PRODI_CHOICES)
    email                           = models.EmailField(null=True, blank=True)

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

    def save(self):
        self.nim = self.nim.upper()
        self.nama = self.nama.title()
        super(Mahasiswa, self).save()

    class Meta :
        ordering = ['nim']

class Dosen(models.Model):
    gelar_depan     = models.CharField(max_length=20)
    nama            = models.CharField(max_length=120)
    gelar_belakang  = models.CharField(max_length=20)
    nidn        = models.CharField(max_length=20, default='1234567890')
    email       = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.nidn

class Penelitian(models.Model):
    dosen       = models.ManyToManyField(Dosen, blank=True)
    mahasiswa   = models.ManyToManyField(Mahasiswa, blank=True)
    judul       = models.CharField(unique=True, max_length=200)
    lokasi      = models.CharField(max_length=120, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('base:detail-penelitian', kwargs={'pk':self.id})

    def get_absolute_url_update(self):
        return reverse('base:update-penelitian', kwargs={'pk':self.id})

    def get_all_mhs_in_penelitian(self):
        return self.mahasiswa.all()

    def __str__(self):
        return self.judul

    def save(self):
        self.judul = self.judul.lower()
        super(Penelitian, self).save()
