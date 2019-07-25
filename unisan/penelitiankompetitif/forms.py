from django.forms import ModelForm
from base.models import Dosen


class DosenDataForm(ModelForm):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    class Meta:
        model = Dosen
        fields = ['gelar_depan', 'nama_lengkap', 'gelar_belakang', 'nidn', 'email', 'program_studi']
