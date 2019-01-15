from django.conf.urls import url

from .views import (
    MahasiswaCreateView,
    MahasiswaDetailView,
    MahasiswaListView,
    MahasiswaUpdateView,
    PenelitianListView,
    PenelitianCreateView,
    PenelitianDetailView,
    PenelitianUpdateView
)

app_name = 'base'
urlpatterns = [
    url(r'^mahasiswa/$', MahasiswaListView.as_view(), name='list-mahasiswa'),
    url(r'^mahasiswa/(?P<pk>\d+)/$', MahasiswaDetailView.as_view(), name='detail-mahasiswa'),
    url(r'^mahasiswa/(?P<pk>\d+)/update/$', MahasiswaUpdateView.as_view(), name='update-mahasiswa'),
    url(r'^create-mahasiswa/$', MahasiswaCreateView.as_view(), name='create-mahasiswa'),
    url(r'^penelitian/$', PenelitianListView.as_view(), name='list-penelitian'),
    url(r'^detail-penelitian/(?P<pk>\d+)/$', PenelitianDetailView.as_view(), name='detail-penelitian'),
    url(r'^update-penelitian/(?P<pk>\d+)/$', PenelitianUpdateView.as_view(), name='update-penelitian'),
    url(r'^create-penelitian/$', PenelitianCreateView.as_view(), name='create-penelitian'),
]
