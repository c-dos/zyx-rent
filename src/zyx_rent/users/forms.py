from django import forms
from django.forms import ModelForm

from .models import Tenant, Property
from utilities.forms import BootstrapMixin


class TenantForm(ModelForm, BootstrapMixin):
    class Meta:
        model = Tenant
        fields = ['name', 'email', 'phone', 'bank', 'account']


class TenantFilterForm(ModelForm, BootstrapMixin):
    model = Tenant


class PropertyForm(ModelForm, BootstrapMixin):
    class Meta:
        model = Property
        fields = ['name', 'address', 'description', 'day_payment', 'price']


class PropertyFilterForm(ModelForm, BootstrapMixin):
    model = Tenant

