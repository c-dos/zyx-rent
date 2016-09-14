import django_filters
from django.db.models import Q
from .models import Tenant, Property
from django.utils.translation import ugettext_lazy as _


class TenantFilter(django_filters.FilterSet):
    q = django_filters.MethodFilter(
        action='search',
        label=_('Search'),
    )

    class Meta:
        model = Tenant
        fields = ['name']

    def search(self, queryset, value):
        return queryset.filter(
            Q(name__icontains=value)
        )


class PropertyFilter(django_filters.FilterSet):
    q = django_filters.MethodFilter(
        action='search',
        label='Search',
    )

    class Meta:
        model = Property
        fields = ['name']

    def search(self, queryset, value):
        return queryset.filter(
            Q(name__icontains=value)
        )
