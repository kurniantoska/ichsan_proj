from django.conf.urls import url
from django.views.generic import TemplateView

from lemlit.views import (
SuraIzinPenelitianMahasiswaDetailView,
SuraIzinPenelitianMahasiswaListView,
SuratIzinPenelitianMahasiswaCreateView,
)

urlpatterns = [
    url(r'^cetak-surat-penelitian-mahasiswa/(?P<pk>\d+)/$', SuraIzinPenelitianMahasiswaDetailView.cetak_pdf, name='cetak-surat-penelitian-mahasiswa'),
    url(r'^list-surat-penelitian-mahasiswa/$', SuraIzinPenelitianMahasiswaListView.as_view(), name='list-surat-penelitian-mahasiswa'),
    url(r'^detail-surat-penelitian-mahasiswa/(?P<pk>\d+)/$', SuraIzinPenelitianMahasiswaDetailView.as_view(), name='detail-surat-penelitian-mahasiswa'),
    url(r'^create-surat-penelitian-mahasiswa/$', SuratIzinPenelitianMahasiswaCreateView.as_view(), name='create-surat-penelitian-mahasiswa'),
    url(r'^surat-penelitian-mahasiswa/$', TemplateView.as_view(template_name='suratpenelitianmahasiswa-home.html'), name='home-surat-penelitian-mahasiswa'),

]