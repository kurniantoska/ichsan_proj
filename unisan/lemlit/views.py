from django.shortcuts import render
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

import json
from django.http import HttpResponse

from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

from base.models import Mahasiswa
from lemlit.models import SuratIzinPenelitianMahasiswa
from .forms import SuraIzinPenelitianMahasiswaCreateForm

# Create your views here.

def get_penelitian_form_mahasiswa(self, mahasiswa=Mahasiswa.objects.get(pk=6)):
    mahasiswa = mahasiswa.penelitian_set.all()
    return mahasiswa


def ajax_region_from_zip(request, mahasiswa):

    # do your logic to lookup the zipcode from the region
    penelitian, lookup_success = get_penelitian_form_mahasiswa(mahasiswa)

    response = Response(content_type='application/json')
    response.write(json.dumps({"success":lookup_success, "penelitian":penelitian}))
    return response

class SuratIzinPenelitianMahasiswaCreateView(CreateView):
    form_class = SuraIzinPenelitianMahasiswaCreateForm
    template_name = 'form.html'

    def get_context_data(self, **kwargs):
        print(kwargs)
        context = super(SuratIzinPenelitianMahasiswaCreateView, self).get_context_data( **kwargs)
        context['penelitian_base_mahasiswa'] = 'Update Data Mahasiswa'
        return context

class SuraIzinPenelitianMahasiswaListView(ListView):
    def get_queryset(self):
        return SuratIzinPenelitianMahasiswa.objects.all()

class SuraIzinPenelitianMahasiswaDetailView(DetailView):
    def get_queryset(self):
        return SuratIzinPenelitianMahasiswa.objects.all()

    def cetak_pdf(self, **kwargs):
        # print(kwargs.get('pk'))
        surat = SuratIzinPenelitianMahasiswa.objects.filter(id=kwargs.get('pk')).first()
        nama_mahasiswa      = surat.penelitian.mahasiswa.first().nama
        nim_mahasiswa       = surat.penelitian.mahasiswa.first().nim
        judul_penelitian    = surat.penelitian.judul
        lokasi_penelitian   = surat.penelitian.lokasi
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="cetak.pdf"'

        # buat objek pdf
        p = canvas.Canvas(response, pagesize=A4)
        width, height = A4

        p.drawString(30,820, 'KEMENTERIAN RISET, TEKNOLOGI DAN PENDIDIKAN TINGGI')
        p.drawString(30,805, 'LEMBAGA PENELITIAN (LEMLIT)')
        p.drawString(30,790, 'UNIVERSITAS ICHSAN GORONTALO')
        p.drawString(30,775, 'Jl. Raden Saleh No. 17 Kota Gorontalo')
        p.drawString(30,760, 'Telp: (0435) 8724466, 829975; Fax: (0435) 82997;')
        p.drawString(30,745, 'E-mail: lembagapenelitian@unisan.ac.id')
        p.drawString(30,700, 'Nomor     : 026/LEMLIT-UNISAN/GTO/VIII/2017')
        p.drawString(30,685, 'Lampiran  : -')

        p.drawString(30, 90, nama_mahasiswa)
        p.drawString(30, 70, nim_mahasiswa)
        p.drawString(30, 50, judul_penelitian)
        p.drawString(30, 30, lokasi_penelitian)

        p.showPage()
        p.save()
        return response