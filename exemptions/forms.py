from django import forms
from exemptions.models import Host, Exemption, User
from django.utils import timezone

class ExemptionForm(forms.ModelForm):
    class Meta:
        model = Exemption
        fields = [ 'requestor', 'authority', 'hosts', 'expires', 'request', 'response', 'approved' ]
        exclude = ('date_approved',)

class HostForm(forms.ModelForm):
    class Meta:
        model = Host
        fields = [ 'name', 'ip', 'unique_id' ]

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [ 'first_name', 'initial', 'last_name', 'email', 'is_authority' ]
