from django.utils.timezone import datetime


FAKULTAS_N_PRODI_CHOICES = (
    ('Fakultas Ekonomi', (
        ('ak', 'Akuntansi'),
        ('man', 'Manajemen'),
        )
     ),
    ('Fakultas Ilmu Komputer', (
        ('ti', 'Teknik Informatika'),
        ('ti', '-'),
    )
    ),
    ('Fakultas Hukum', (
        ('hu', 'Ilmu Hukum'),
        ('hu', '-'),
    )
    ),
    ('Fakultas Teknik', (
        ('ar', 'Arsitektur'),
        ('el', 'Elektro'),
    )
    ),
    ('Fakultas Ilmu Sosial, Ilmu Politik', (
        ('ko', 'Komunikasi'),
        ('ip', 'Ilmu Pemerintahan'),
    )
    ),
    ('Fakultas Pertanian', (
        ('agb', 'Agribisnis'),
        ('agr', 'Agroteknologi'),
        ('thp', 'Teknologi Hasil Pertanian'),
    ),
    )
)


def periode(tahun: int) -> tuple:
    """
    input tahun
    :param tahun:
    :return:
    tuple 1 dengan 2 element range tanggal 'start gasal', 'end gasal'
    tuple 2 dengan 2 element range tanggal 'start genap', 'end genap'
    """
    tahun_ini = tahun
    tahun_lalu = tahun_ini - 1
    genap_start = datetime.strptime('27-01-{}'.format(tahun_ini), '%d-%m-%Y')
    genap_end = datetime.strptime('29-01-{}'.format(tahun_ini), '%d-%m-%Y')
    gasal_start = datetime.strptime('27-07-{}'.format(tahun_lalu), '%d-%m-%Y')
    gasal_end = datetime.strptime('29-01-{}'.format(tahun_lalu), '%d-%m-%Y')
    return (gasal_start, gasal_end), (genap_start, genap_end)
