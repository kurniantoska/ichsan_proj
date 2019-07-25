from django.views import generic
from django.http import JsonResponse
from base.models import Dosen
from penelitiankompetitif.forms import DosenDataForm
from django.urls import reverse_lazy


class AjaxableResponseMixin:
    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return JsonResponse(data)
        else:
            return response


class IsiDataDosen(generic.FormView):
    model = Dosen
    template_name = 'biodata_dosen.html'
    form_class = DosenDataForm
    success_url = reverse_lazy('pen_komp:isi_data_dosen')


class UploadProposal(generic.View):
    pass
