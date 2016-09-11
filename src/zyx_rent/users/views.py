from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count, Q
from django.views import generic
from .models import Tenant
from .forms import TenantForm, TenantFilterForm
from django.core.urlresolvers import reverse_lazy
from utilities.views import ObjectEditView, ObjectListView
from . import tables, filters, forms


@login_required(login_url="login/")
def index(request):
    return render(request, "home.html")


class LoginView(LoginRequiredMixin, generic.View):
    login_url = '/users/login/'
    redirect_field_name = 'next'


# Tenant
class TenantEditView(LoginRequiredMixin, ObjectEditView):
    model = Tenant
    form_class = TenantForm
    success_url = reverse_lazy('tenant_list')
    template_name = 'tenants/add.html'
    cancel_url = 'tenant_list'
    column_created_by = 'user'


class TenantListView(LoginView, ObjectListView):
    queryset = Tenant.objects.order_by('-id')
    table = tables.TenantTable
    template_name = 'tenants/list.html'
    filter = filters.TenantFilter

    # Hook filter by request
    def alter_queryset(self, request):
        return self.queryset.filter(user=request.user).all()


def tenant(request, pk):
    tenant = get_object_or_404(Tenant, pk=pk)
    return render(request, 'tenants/show.html', {
        'tenant': tenant,
    })
