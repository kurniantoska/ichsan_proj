from django.contrib import admin
from .models import (
SuratIzinPenelitianMahasiswa,
PetugasAdmininistrasi,
StrukturManajemen,
)

class SuratIzinPenelitianMahasiswaAdmin(admin.ModelAdmin):
   list_display = ('petugas', 'mahasiswa')
   search_fields = ['petugas']

# Register your models here.
admin.site.register(SuratIzinPenelitianMahasiswa, SuratIzinPenelitianMahasiswaAdmin)
admin.site.register(PetugasAdmininistrasi)
admin.site.register(StrukturManajemen)
