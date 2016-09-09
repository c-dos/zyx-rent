import django_tables2 as tables
from django_tables2.utils import Accessor
from utilities.tables import BaseTable, ToggleColumn
from .models import Tenant


TENANTGROUP_ACTIONS = """
{% if perms.tenancy.change_tenantgroup %}
    <a href="{% url 'tenancy:tenantgroup_edit' slug=record.slug %}" class="btn btn-xs btn-warning"><i class="glyphicon glyphicon-pencil" aria-hidden="true"></i></a>
{% endif %}
"""


#
# Tenants
#
class TenantTable(BaseTable):
    id = ToggleColumn()
    # name = tables.LinkColumn('tenancy:tenant', args=[Accessor('slug')], verbose_name='Name')
    name = tables.Column(verbose_name='Name')
    email = tables.Column(verbose_name='Email')
    # description = tables.Column(verbose_name='Description')

    class Meta(BaseTable.Meta):
        model = Tenant
        fields = ('id', 'name', 'email')
