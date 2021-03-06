"""unisan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
from django.views.generic import TemplateView

from base.views import (
    MahasiswaAutoComplete,
    PenelitianBaseFromMahasiswaAutoComplete,
    Profile,
)


urlpatterns = [
    path('', include('penelitiankompetitif.urls')),
    path('accounts/profile/', TemplateView.as_view(template_name='profiles.html'), name='profile'),
    path('accounts/', include('allauth.urls')),
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^cari-data/$', TemplateView.as_view(template_name='halamandata.html'), name='cari-data'),
    url(r'^admin/', admin.site.urls),
    url(r'^lemlit/', include('lemlit.urls')),
    url(r'^data/', include('base.urls')),
    url(r'^api-mhs-get/$', MahasiswaAutoComplete.as_view(), name='autocomplete-mahasiswa'),
    url(
        r'^api-penelitian-get/$',
        PenelitianBaseFromMahasiswaAutoComplete.as_view(),
        name='autocomplete-penelitian-base-mahasiswa'
    ),
    path(
        'hibahpenelitian',
        TemplateView.as_view(template_name='simple/base-simple.html'),
        name='hibah-penelitian-home'
    )

]
