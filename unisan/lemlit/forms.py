# lemlit/forms.py

from django import forms
from .models import SuratIzinPenelitianMahasiswa

class SuraIzinPenelitianMahasiswaCreateForm(forms.ModelForm):
    class Meta:

        model = SuratIzinPenelitianMahasiswa
        fields = [
            'disetujui',
            'penelitian',
        ]