import django_tables2 as tables
from django_tables2.utils import Accessor
from utilities.tables import BaseTable, ToggleColumn
from .models import Tenant, Property
from django.utils.translation import ugettext_lazy as _

#
# Tenants
#
class TenantTable(BaseTable):
    name = tables.LinkColumn('tenant', args=[Accessor('pk')], verbose_name=_('Name'))
    email = tables.Column(verbose_name='Email')

    class Meta(BaseTable.Meta):
        model = Tenant
        fields = ('name', 'email')

#
# Properties
#
class PropertyTable(BaseTable):
    name = tables.LinkColumn('property', args=[Accessor('pk')], verbose_name='Name')
    address = tables.Column(verbose_name='Address')
    description = tables.Column(verbose_name='Description')
    day_payment = tables.Column(verbose_name='Day of Payment')
    price = tables.Column(verbose_name='Price')

    class Meta(BaseTable.Meta):
        model = Property
        fields = ('name', 'address', 'description', 'day_payment', 'price')
