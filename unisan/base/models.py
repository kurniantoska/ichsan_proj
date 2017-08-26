
from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.

class Mahasiswa(models.Model):
    nama        = models.CharField(max_length=120)
    nim         = models.CharField(unique=True, max_length=15)
    email       = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.nim

    def get_nama(self):
        return self.nama

    def get_absolute_url(self):
        return reverse('base:detail-mahasiswa', kwargs={'pk': self.id})

    class Meta :
        ordering = ['nim']

class Dosen(models.Model):
    nama        = models.CharField(max_length=120)
    nidn        = models.CharField(max_length=20, default='1234567890')
    email       = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.nidn

class Penelitian(models.Model):
    dosen       = models.ManyToManyField(Dosen, null=True, blank=True)
    mahasiswa   = models.ManyToManyField(Mahasiswa, null=True, blank=True)
    judul       = models.CharField(max_length=200)
    lokasi      = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self):
        return "{} - {}".format(self.mahasiswa.first(), self.judul)