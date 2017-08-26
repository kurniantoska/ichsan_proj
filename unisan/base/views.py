from dal import autocomplete

from django.shortcuts import render

from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .forms import MahasiswaCreateForm, PenelitianCreateForm

from .models import Mahasiswa, Penelitian
# Create your views here.

class MahasiswaCreateView(CreateView):
    form_class = MahasiswaCreateForm
    template_name = 'mahasiswa-form.html'

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

class MahasiswaAutoComplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Mahasiswa.objects.all()

        if self.q :
            qs = qs.filter(nim__icontains=self.q)

        return qs