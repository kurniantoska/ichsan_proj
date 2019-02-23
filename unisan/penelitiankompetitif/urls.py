from django.urls import path
from django.views.generic import TemplateView


app_name = 'pen_komp'
urlpatterns = [
    path(
        'penelitian_kompetitif/',
        TemplateView.as_view(template_name='home_penelitian.html'),
        name='home_pen'
    ),
]