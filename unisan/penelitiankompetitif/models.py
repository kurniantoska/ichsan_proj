from django.utils.timezone import datetime

from django.db import models
from base.models import (
    Dosen,
    Penelitian
)


# Create your models here.
class PenelitianKompetitif(models.Model):
    pil_periode = (
        ('genap', 'Genap'),
        ('gasal', 'Gasal'),
    )
    periode = models.CharField(choices=pil_periode, max_length=5)
    tahun = models.CharField(default=datetime.now().year, max_length=4)

    Dosen = models.ForeignKey(
        Dosen,
        on_delete=models.CASCADE,
        related_name='nama_dosen')

    Penelitian = models.ForeignKey(
        Penelitian,
        on_delete=models.CASCADE,
        related_name='penelitian_dosen_kompetitif'
    )

    berkas_proposal = models.FileField(upload_to='penelitian_kompetitif')
    berkas_laporan = models.FileField(upload_to='penelitian_kompetitif')
    berkas_publikasi = models.FileField(upload_to='penelitian_kompetitif')
