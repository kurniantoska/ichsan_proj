from dal import autocomplete

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView

from .forms import MahasiswaCreateForm, PenelitianCreateForm

from .models import Mahasiswa, Penelitian
from lemlit.models import SuratIzinPenelitianMahasiswa


class Profile(DetailView):
    template_name = 'profiles.html'


class MahasiswaCreateView(LoginRequiredMixin, CreateView):
    form_class = MahasiswaCreateForm
    template_name = 'mahasiswa-form.html'

    def get_context_data(self, **kwargs):
        context = super(MahasiswaCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Tambah Data Mahasiswa'
        return context


class MahasiswaUpdateView(LoginRequiredMixin, UpdateView):
    form_class = MahasiswaCreateForm
    template_name = 'mahasiswa-form.html'

    def get_queryset(self):
        return Mahasiswa.objects.all()

    def get_context_data(self, **kwargs):
        context = super(MahasiswaUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Update Data Mahasiswa'
        return context


class MahasiswaListView(ListView):
    def get_queryset(self):
        return Mahasiswa.objects.all()

    def get_context_data(self, **kwargs):

        context = super(MahasiswaListView, self).get_context_data(**kwargs)
        context['temp'] = self.request.GET.get('temp')

        mhs = self.get_queryset()
        paginator = Paginator(mhs, 2)
        page = self.request.GET.get('page')

        try:
            mhs = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            mhs = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            mhs = paginator.page(paginator.num_pages)

        context['mhs'] = mhs

        return context


class MahasiswaDetailView(DetailView):
    def get_queryset(self):
        return Mahasiswa.objects.all()


class PenelitianCreateView(LoginRequiredMixin, CreateView):
    form_class = PenelitianCreateForm
    template_name = 'penelitian-form.html'


class PenelitianUpdateView(LoginRequiredMixin, UpdateView):
    model = Penelitian
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
            context = super(MahasiswaHavePenelitianDetailView, self).get_context_data(**kwargs)
            context['title'] = 'Update Data Mahasiswa'
            return context


class MahasiswaAutoComplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Mahasiswa.objects.all()

        if self.q:
            qs = qs.filter(nim__icontains=self.q)

        return qs


class PenelitianBaseFromMahasiswaAutoComplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        semua_mahasiswa = Mahasiswa.objects.all()

        mhs_pk = self.forwarded.get('mhs', None)
        # debug
        # print('nilai mhs_pk -> {} '.format(mhs_pk))
        qs = None
        if mhs_pk:
            mhs_instance = semua_mahasiswa.get(pk=mhs_pk)
            list_penelitian_mhs_instance = Penelitian.objects.filter(mahasiswa=mhs_instance)
            # surat_izin_on_db = SuratIzinPenelitianMahasiswa.objects.filter(mahasiswa=mhs_instance)
            list_penelitian_mhs_not_exists_in_suratizinpenelitianmahasiswa = list_penelitian_mhs_instance.exclude(
                suratizinpenelitianmahasiswa__mahasiswa=mhs_instance
            )
            qs = list_penelitian_mhs_not_exists_in_suratizinpenelitianmahasiswa

        if self.q:
            qs = qs.filter(judul__icontains=self.q)

        return qs
