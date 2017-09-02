import string

def get_fakultas_full_name(program_studi):
    if program_studi in ('ak', 'man'):
        return 'Fakultas Ekonomoi'
    elif program_studi in ('ar', 'el'):
        return  'Fakultas Teknik'
    else:
        return 'Fakultas tidak terdaftar pada sistem kami!'

def get_program_studi_full_name(program_studi):
    if program_studi == 'ak':
        return 'Akuntansi'
    elif program_studi in ('man'):
        return  'Manajemen'
    else:
        return 'Fakultas tidak terdaftar pada sistem kami!'
