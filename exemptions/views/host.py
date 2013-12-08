from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from exemptions.models import Host

class HostList(ListView):
    model = Host

class HostCreate(CreateView):
    model = Host
    success_url = reverse_lazy('host_list')

class HostUpdate(UpdateView):
    model = Host
    success_url = reverse_lazy('host_list')

class HostDelete(DeleteView):
    model = Host
    success_url = reverse_lazy('host_list')
