from django.core.exceptions import PermissionDenied
import functools

def get_program_studi_full_name(program_studi):
    PROGRAM_STUDI_DICT = {
        'agb': 'Agribisnis',
        'agr': 'Agroteknologi',
        'ak': 'Akuntansi',
        'hu': 'Ilmu Hukum',
        'ko': 'Ilmu Komunikasi',
        'ip': 'Ilmu Pemerintahan',
        'man': 'Manajemen',
        'ar': 'Teknik Arsitektur',
        'el': 'Teknik Elektro',
        'ti': 'Teknik Informatika',
        'thp': 'Teknologi Hasil Pertanian'
    }
    return PROGRAM_STUDI_DICT[program_studi]


def check_operator(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        if not self.request.user.groups.filter(name__in=['operator', ]):
            raise PermissionDenied
        return func(self, *args, **kwargs)
    return wrapper
