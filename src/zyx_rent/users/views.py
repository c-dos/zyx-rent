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


@login_required(login_url="/users/login/")
def index(request):
    return render(request, "home.html")


class LoginView(LoginRequiredMixin, generic.View):
    login_url = '/users/login/'
    redirect_field_name = 'next'


# Tenant
class TenantEditView(LoginView, ObjectEditView):
    model = Tenant
    form_class = TenantForm
    success_url = reverse_lazy('tenant_list')
    template_name = 'tenants/add.html'
    cancel_url = 'tenant_list'
    column_created_by = 'user'

    def get_object(self, kwargs, request):
        return get_object_or_404(self.model, pk=kwargs['pk'],
                                 user=request.user)


class TenantListView(LoginView, ObjectListView):
    queryset = Tenant.objects.order_by('-id')
    table = tables.TenantTable
    template_name = 'tenants/list.html'
    filter = filters.TenantFilter

    # Hook filter by request
    def alter_queryset(self, request):
        return self.queryset.filter(user=request.user).all()


@login_required(login_url="/users/login/")
def tenant(request, pk):
    queryset = Tenant.objects.filter(user=request.user)
    tenant = get_object_or_404(queryset, pk=pk)
    return render(request, 'tenants/show.html', {
        'tenant': tenant,
    })
