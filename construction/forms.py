from django import forms
from .models import contact_info

class contactInfoForms(forms.ModelForm):
    class Meta:
        model = contact_info
        fields = ('first_name', 'last_name', 'e_mail_address', 'message')
        