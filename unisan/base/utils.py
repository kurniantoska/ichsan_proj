def get_program_studi_full_name(program_studi):
    PROGRAM_STUDI_DICT = {'ak' : 'Akuntansi',
                          'man' : 'Manajemen',
                          'si' : 'Sistem Informasi',
                          'ti' : 'Teknik Informatika',
                          'ar' : 'Arsitektur',
                          'el' : 'Teknik Elektro',
                          'ko' : 'Ilmu Komunikasi',
                          'ab' : 'Agribisnis',
                          'thp' : 'Teknologi Hasil Pertanian'
                          }
    return PROGRAM_STUDI_DICT[program_studi]
