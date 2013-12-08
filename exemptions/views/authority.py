from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from exemptions.models import Authority

class AuthorityList(ListView):
    model = Authority

class AuthorityCreate(CreateView):
    model = Authority
    success_url = reverse_lazy('authority_list')

class AuthorityUpdate(UpdateView):
    model = Authority
    success_url = reverse_lazy('authority_list')

class AuthorityDelete(DeleteView):
    model = Authority
    success_url = reverse_lazy('authority_list')
