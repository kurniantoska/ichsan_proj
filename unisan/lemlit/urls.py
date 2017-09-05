from django.conf.urls import url
from django.views.generic import TemplateView

from lemlit.views import (
SuraIzinPenelitianMahasiswaDetailView,
SuraIzinPenelitianMahasiswaListView,
SuratIzinPenelitianMahasiswaCreateView,
SuratIzinPenelitianMahasiswaUpdateView,
SuratIzinPenelitianMahasiswaDeleteView,
SuratKeteranganPenelitianMahasiswaCreateView,
CetakSuratIzinPenelitianMahasiswa,
CetakSuratKeteranganPenelitianMahasiswa,
)

urlpatterns = [
    url(r'^list-surat-penelitian-mahasiswa/$', SuraIzinPenelitianMahasiswaListView.as_view(), name='list-surat-penelitian-mahasiswa'),
    url(r'^detail-surat-penelitian-mahasiswa/(?P<pk>\d+)/$', SuraIzinPenelitianMahasiswaDetailView.as_view(), name='detail-surat-penelitian-mahasiswa'),
    url(r'^edit-surat-penelitian-mahasiswa/(?P<pk>\d+)/edit/$', SuratIzinPenelitianMahasiswaUpdateView.as_view(), name='edit-surat-penelitian-mahasiswa'),
    url(r'^cetak-surat-penelitian-mahasiswa/(?P<pk>\d+)/$', CetakSuratIzinPenelitianMahasiswa.as_view(), name='cetak-surat-izin-penelitian-mahasiswa'),
    url(r'^ctk-srt-ket-pen-mhs/(?P<pk>\d+)/$', CetakSuratKeteranganPenelitianMahasiswa.as_view(), name='cetak-surat-keterangan-penelitian-mahasiswa'),
    url(r'^create-surat-penelitian-mahasiswa/$', SuratIzinPenelitianMahasiswaCreateView.as_view(), name='create-surat-penelitian-mahasiswa'),
    url(r'^create-surat-keterangan-pmhs/$', SuratKeteranganPenelitianMahasiswaCreateView.as_view(), name='create-surat-keterangan-pmhs'),
    url(r'^surat-penelitian-mahasiswa/$', TemplateView.as_view(template_name='suratpenelitianmahasiswa-home.html'), name='home-surat-penelitian-mahasiswa'),
    url(r'^delete-surat-penelitian-mahasiswa/(?P<pk>\d+)/$', SuratIzinPenelitianMahasiswaDeleteView.as_view(), name='delete-surat-penelitian-mahasiswa'),
]