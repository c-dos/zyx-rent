from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'home', views.index, name='home'),

    # tenant
    url(r'^tenant/add/$', views.TenantAddView.as_view(), name='tenant_add'),
    url(r'^tenant/$', views.TenantListView.as_view(), name='tenant_list')


]
