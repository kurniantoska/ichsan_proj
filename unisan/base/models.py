
from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.

class Mahasiswa(models.Model):
    FAKULTAS_N_PRODI_CHOICES = (
        ('Fakultas Ekonomi', (
            ('ak', 'Akuntansi'),
            ('man', 'Manajemen'),
            )
        ),
        ('Fakultas Teknik', (
            ('ar', 'Arsitektur'),
            ('el', 'Elektro'),
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


    class Meta :
        ordering = ['nim']

class Dosen(models.Model):
    nama        = models.CharField(max_length=120)
    nidn        = models.CharField(max_length=20, default='1234567890')
    email       = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.nidn

class Penelitian(models.Model):
    dosen       = models.ManyToManyField(Dosen, blank=True)
    mahasiswa   = models.ManyToManyField(Mahasiswa, blank=True)
    judul       = models.CharField(max_length=200)
    lokasi      = models.CharField(max_length=120, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('base:detail-penelitian', kwargs={'pk':self.id})

    def __str__(self):
        return self.judul