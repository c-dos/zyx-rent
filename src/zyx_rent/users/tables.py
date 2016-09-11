import django_tables2 as tables
from django_tables2.utils import Accessor
from utilities.tables import BaseTable, ToggleColumn
from .models import Tenant


#
# Tenants
#
class TenantTable(BaseTable):
    name = tables.LinkColumn('tenant', args=[Accessor('pk')], verbose_name='Name')
    email = tables.Column(verbose_name='Email')

    class Meta(BaseTable.Meta):
        model = Tenant
        fields = ('name', 'email')
