from django import forms
from exemptions.models import Host, Exemption, Authority
from django.utils import timezone

class ExemptionForm(forms.ModelForm):
    class Meta:
        model = Exemption
        fields = [ 'authority', 'hosts', 'expires', 'request', 'response', 'approved' ]

    def clean_expires(self):
        expires = self.cleaned_data['expires']
        if expires < timezone.now():
            raise forms.ValidationError("The exemption expiration cannot be in the past!")
        return expires

class HostForm(forms.ModelForm):
    class Meta:
        model = Host
        fields = [ 'name', 'ip', 'unique_id' ]

class AuthorityForm(forms.ModelForm):
    class Meta:
        model = Authority
        fields = [ 'first_name', 'initial', 'last_name', 'email' ]
