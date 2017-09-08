# lemlit/forms.py

from dal import autocomplete
from dal import forward

from django import forms
from base.models import Mahasiswa, Penelitian
from .models import (
SuratIzinPenelitianMahasiswa,
SuratKeteranganPenelitianMahasiswa
)

class SuraIzinPenelitianMahasiswaCreateForm(forms.ModelForm):
    mahasiswa = forms.ModelChoiceField(
        queryset=Mahasiswa.objects.all(),
        widget=autocomplete.ModelSelect2(url='autocomplete-mahasiswa')
    )

    penelitian = forms.ModelChoiceField(
        queryset = Penelitian.objects.all(),
        widget = autocomplete.ModelSelect2(url='autocomplete-penelitian-base-mahasiswa', forward=(forward.Field('mahasiswa','mhs'),))
    )

    class Meta:
        model = SuratIzinPenelitianMahasiswa
        fields = (
            'mahasiswa',
            'penelitian',
            'nomor_surat',
            'nama_instansi',
            'tujuan_surat',
            'petugas'
        )

        widgets = {

            'nomor_surat': forms.TextInput(
                attrs={'placeholder': 'Tiga digit nomor surat : XXX '}),
            'tujuan_surat': forms.TextInput(
                attrs={'placeholder': 'Gorontalo'}),
            'nama_instansi': forms.TextInput(
                attrs={'placeholder': 'Nama Kantor / Lembaga / Perusahaan'}),
            'petugas': forms.TextInput(
                attrs={'placeholder': 'Nama Petugas Lemlit'}),
        }


class SuraKeteranganPenelitianMahasiswaCreateForm(SuraIzinPenelitianMahasiswaCreateForm):
    class Meta:
        model = SuratKeteranganPenelitianMahasiswa
        fields = (
            'mahasiswa',
            'penelitian',
            'nomor_surat',
            'nama_instansi',
            'tujuan_surat',
        )