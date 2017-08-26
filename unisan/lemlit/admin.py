from django.contrib import admin
from .models import (
SuratIzinPenelitianMahasiswa,
PetugasAdmininistrasi,
StrukturManajemen,
)

# Register your models here.
admin.site.register(SuratIzinPenelitianMahasiswa)
admin.site.register(PetugasAdmininistrasi)
admin.site.register(StrukturManajemen)
