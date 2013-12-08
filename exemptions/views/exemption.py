from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from exemptions.models import Exemption

class ExemptionList(ListView):
    model = Exemption

class ExemptionCreate(CreateView):
    model = Exemption
    success_url = reverse_lazy('exemption_list')

class ExemptionUpdate(UpdateView):
    model = Exemption
    success_url = reverse_lazy('exemption_list')

class ExemptionDelete(DeleteView):
    model = Exemption
    success_url = reverse_lazy('exemption_list')
