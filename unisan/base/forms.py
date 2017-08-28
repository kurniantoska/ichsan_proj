# base/forms.py

from dal import autocomplete

from django import forms
from .models import Mahasiswa, Penelitian

class MahasiswaCreateForm(forms.ModelForm):

    class Meta:
        model = Mahasiswa
        fields = [
            'nama',
            'nim',
            'email',
        ]


class PenelitianCreateForm(forms.ModelForm):
    class Meta:
        model = Penelitian
        fields = (
            'mahasiswa',
            'judul',
            'lokasi',
        )

        widgets = {
            'mahasiswa': autocomplete.ModelSelect2(url='autocomplete-mahasiswa')
        }