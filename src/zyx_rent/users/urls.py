from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'home', views.index, name='home'),

    # tenant
    url(r'^tenant/add/$', views.TenantEditView.as_view(), name='tenant_add'),
    url(r'^tenant/$', views.TenantListView.as_view(), name='tenant_list'),
    url(r'^tenant/(?P<pk>[\w-]+)/$', views.tenant, name='tenant'),
    url(r'^tenant/(?P<pk>[\w-]+)/edit/$', views.TenantEditView.as_view(), name='tenant_edit'),

    # property
    url(r'^property/add/$', views.PropertyEditView.as_view(), name='property_add'),
    url(r'^property/$', views.PropertyListView.as_view(), name='property_list'),
    url(r'^property/(?P<pk>[\w-]+)/$', views.property, name='property'),
    url(r'^property/(?P<pk>[\w-]+)/edit/$', views.PropertyEditView.as_view(), name='property_edit')

]
