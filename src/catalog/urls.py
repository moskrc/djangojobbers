from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('catalog.views',
    url(r'^$', 'index', name='home'),
    url(r'^add/$', 'add', name='catalog_add'),
    url(r'^(?P<item_id>\d+)/$', 'view', name='catalog_view'),
    url(r'^(?P<item_id>\d+)/edit/(?P<secret_key>.+)/$', 'edit', name='catalog_edit'),
    url(r'^(?P<item_id>\d+)/delete/(?P<secret_key>.+)/$', 'delete', name='catalog_delete'),
    url(r'^subscribe/$', 'subscribe', name='catalog_subscribe'),
)
