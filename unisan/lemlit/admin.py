from django.contrib import admin
from .models import (
   SuratIzinPenelitianMahasiswa,
   PetugasAdmininistrasi,
   StrukturManajemen,
   HibahPenelitian,
   Status,
   Pengumuman,
)


@admin.register(SuratIzinPenelitianMahasiswa)
class SuratIzinPenelitianMahasiswaAdmin(admin.ModelAdmin):
    list_display = ('petugas', 'mahasiswa')
    search_fields = ['petugas']


@admin.register(HibahPenelitian)
class HibahPenelitianAdmin(admin.ModelAdmin):
    pass


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    pass


@admin.register(Pengumuman)
class PengumumanAdmin(admin.ModelAdmin):
    pass


admin.site.register(PetugasAdmininistrasi)
admin.site.register(StrukturManajemen)
