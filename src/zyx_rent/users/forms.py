from django import forms
from django.forms import ModelForm

from .models import Tenant
from utilities.forms import BootstrapMixin

class TenantForm(ModelForm, BootstrapMixin):
    class Meta:
        model = Tenant
        fields = ['name', 'email', 'phone', 'bank', 'account']

class TenantFilterForm(ModelForm, BootstrapMixin):
    model = Tenant
