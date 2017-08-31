from dal import autocomplete
from urllib import parse
from django.shortcuts import render

from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from .forms import MahasiswaCreateForm, PenelitianCreateForm

from .models import Mahasiswa, Penelitian
from lemlit.models import SuratIzinPenelitianMahasiswa
# Create your views here.

class MahasiswaCreateView(CreateView):
    form_class = MahasiswaCreateForm
    template_name = 'mahasiswa-form.html'

    def get_context_data(self, **kwargs):
        context = super(MahasiswaCreateView, self).get_context_data( **kwargs)
        context['title'] = 'Tambah Data Mahasiswa'
        return context

class MahasiswaUpdateView(UpdateView):
    form_class = MahasiswaCreateForm
    template_name = 'mahasiswa-form.html'

    def get_queryset(self):
        return Mahasiswa.objects.all()

    def get_context_data(self, **kwargs):
        context = super(MahasiswaUpdateView, self).get_context_data( **kwargs)
        context['title'] = 'Update Data Mahasiswa'
        return context


class MahasiswaListView(ListView):
    def get_queryset(self):
        return Mahasiswa.objects.all()

class MahasiswaDetailView(DetailView):
    def get_queryset(self):
        return Mahasiswa.objects.all()


class PenelitianCreateView(CreateView):
    form_class = PenelitianCreateForm
    template_name = 'penelitian-form.html'

class PenelitianListView(ListView):
    def get_queryset(self):
        return Penelitian.objects.all()

class PenelitianDetailView(DetailView):
    def get_queryset(self):
        return Penelitian.objects.all()

class MahasiswaHavePenelitianDetailView(DetailView):
    def get_queryset(self):
        return Mahasiswa.objects.none()
    def get_context_data(self, **kwargs):
            context = super(MahasiswaUpdateView, self).get_context_data(**kwargs)
            context['title'] = 'Update Data Mahasiswa'
            return context


class MahasiswaAutoComplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Mahasiswa.objects.all()

        if self.q :
            qs = qs.filter(nim__icontains=self.q)

        return qs

class PenelitianBaseFromMahasiswaAutoComplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        semua_mahasiswa = Mahasiswa.objects.all()

        mhs_pk = self.forwarded.get('mhs', None)
        # debug
        # print('nilai mhs_pk -> {} '.format(mhs_pk))
        if mhs_pk :
            mhs_instance = semua_mahasiswa.get(pk=mhs_pk)
            list_penelitian_mhs_instance = Penelitian.objects.filter(mahasiswa=mhs_instance)
            list_penelitian_mhs_instance_not_exists_in_suratizinpenelitianmahasiswa = list_penelitian_mhs_instance.exclude(suratizinpenelitianmahasiswa__isnull=False)
            qs = list_penelitian_mhs_instance_not_exists_in_suratizinpenelitianmahasiswa

        if self.q :
            qs = qs.filter(judul__icontains=self.q)

        return qs