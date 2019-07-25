from django.urls import path
from django.views.generic import TemplateView
from penelitiankompetitif.views import IsiDataDosen

app_name = 'pen_komp'
urlpatterns = [
    path(
        'penelitian_kompetitif/',
        TemplateView.as_view(template_name='home_penelitian.html'),
        name='home_pen'
    ),
    path(
        'isi_biodata_dosen/',
        IsiDataDosen.as_view(),
        name='isi_data_dosen'
    ),
]
