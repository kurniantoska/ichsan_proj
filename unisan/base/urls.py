from django.conf.urls import url

from .views import (
MahasiswaCreateView,
MahasiswaDetailView,
MahasiswaListView,
PenelitianListView,
PenelitianCreateView,
)

urlpatterns = [
    url(r'^mahasiswa/$', MahasiswaListView.as_view(), name='list-mahasiswa'),
    url(r'^mahasiswa/(?P<pk>\d+)/$', MahasiswaDetailView.as_view(), name='detail-mahasiswa'),
    url(r'^create-mahasiswa/$', MahasiswaCreateView.as_view(), name='create-mahasiswa'),
    url(r'^list-penelitian/$', PenelitianListView.as_view(), name='list-penelitian'),
    url(r'^create-penelitian/$', PenelitianCreateView.as_view(), name='create-penelitian'),


]