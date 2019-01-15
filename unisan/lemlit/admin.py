from django.contrib import admin
from .models import (
   SuratIzinPenelitianMahasiswa,
   PetugasAdmininistrasi,
   StrukturManajemen,
)


@admin.register(SuratIzinPenelitianMahasiswa)
class SuratIzinPenelitianMahasiswaAdmin(admin.ModelAdmin):
    list_display = ('petugas', 'mahasiswa')
    search_fields = ['petugas']


admin.site.register(PetugasAdmininistrasi)
admin.site.register(StrukturManajemen)
