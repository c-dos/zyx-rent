from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Tenant
from .forms import TenantForm
from django.core.urlresolvers import reverse_lazy
from utilities.views import ObjectEditView

@login_required(login_url="login/")
def index(request):
    return render(request, "home.html")


class LoginView(LoginRequiredMixin, generic.View):
    login_url = '/users/login/'
    redirect_field_name = 'next'


# Tenant
class TenantAddView(LoginRequiredMixin, ObjectEditView):
    model = Tenant
    form_class = TenantForm
    success_url = reverse_lazy('tenant_list')
    template_name = 'tenants/add.html'
    cancel_url = 'tenant_list'
    column_created_by = 'user'


class TenantListView(LoginView, generic.ListView):
    model = Tenant
    template_name = 'tenants/list.html'

    def get_queryset(self):
        """Return the last five tenant of user."""
        return Tenant.objects.filter(user=self.request.user).order_by('-id')[:5]
