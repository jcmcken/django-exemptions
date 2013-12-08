from django import forms
from exemptions.models import Host, Exemption, Authority
from django.utils import timezone

class ExemptionForm(forms.ModelForm):
    class Meta:
        model = Exemption
        fields = [ 'authority', 'hosts', 'expires', 'request', 'response', 'approved' ]

class HostForm(forms.ModelForm):
    class Meta:
        model = Host
        fields = [ 'name', 'ip', 'unique_id' ]

class AuthorityForm(forms.ModelForm):
    class Meta:
        model = Authority
        fields = [ 'first_name', 'initial', 'last_name', 'email' ]
