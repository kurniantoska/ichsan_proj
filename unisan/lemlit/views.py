from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from django.core.exceptions import PermissionDenied

from base.utils import check_operator

from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from lemlit.models import (
    SuratIzinPenelitianMahasiswa,
)
from .forms import (
    SuraIzinPenelitianMahasiswaCreateForm,
    SuraKeteranganPenelitianMahasiswaCreateForm
)


class SuratIzinPenelitianMahasiswaCreateView(LoginRequiredMixin, CreateView):
    form_class = SuraIzinPenelitianMahasiswaCreateForm
    template_name = 'form-surat-izin-penelitian-mhs.html'

    @check_operator
    def get_context_data(self, **kwargs):
        context = super(SuratIzinPenelitianMahasiswaCreateView, self).get_context_data()
        context['status'] = 'Pengajuan'
        return context


class SuratKeteranganPenelitianMahasiswaCreateView(LoginRequiredMixin, CreateView):
    form_class = SuraKeteranganPenelitianMahasiswaCreateForm
    template_name = 'form-surat-izin-penelitian-mhs.html'

    @check_operator
    def get_context_data(self, **kwargs):
        context = super(SuratKeteranganPenelitianMahasiswaCreateView, self).get_context_data()
        context['status'] = 'Pengajuan Surat Keterangan'
        return context


class SuratIzinPenelitianMahasiswaUpdateView(LoginRequiredMixin, UpdateView):
    """Surat izin penelitian mahasiswa"""
    model = SuratIzinPenelitianMahasiswa
    form_class = SuraIzinPenelitianMahasiswaCreateForm
    template_name = 'form-surat-izin-penelitian-mhs.html'

    @check_operator
    def get_context_data(self, **kwargs):
        context = super(SuratIzinPenelitianMahasiswaUpdateView, self).get_context_data()
        context['status'] = 'Edit'
        return context


class SuratIzinPenelitianMahasiswaDeleteView(LoginRequiredMixin, DeleteView):
    model = SuratIzinPenelitianMahasiswa
    success_url = reverse_lazy('lemlit:list-surat-penelitian-mahasiswa')

    @check_operator
    def get_context_data(self, **kwargs):
        context = super(SuratIzinPenelitianMahasiswaDeleteView, self).get_context_data()
        return context


class SuraIzinPenelitianMahasiswaListView(ListView):
    def get_queryset(self):
        return SuratIzinPenelitianMahasiswa.objects.all()


class SuraIzinPenelitianMahasiswaDetailView(DetailView):
    def get_queryset(self):
        return SuratIzinPenelitianMahasiswa.objects.all()


class CetakSuratIzinPenelitianMahasiswa(DetailView):
    model = SuratIzinPenelitianMahasiswa
    template_name = "lemlit/cetak-surat-izin-penelitian-mahasiswa.html"


class CetakKuitansiSuratPenelitian(DetailView):
    model = SuratIzinPenelitianMahasiswa
    template_name = "lemlit/cetak-kuitansi-penelitian-mahasiswa.html"


class CetakSuratKeteranganPenelitianMahasiswa(DetailView):
    model = SuratIzinPenelitianMahasiswa
    template_name = "lemlit/cetak-surat-keterangan-penelitian-mahasiswa.html"
