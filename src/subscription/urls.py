from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('subscription.views',
    url(r'^add/$', 'subscribe', name='subscribe_add'),
    url(r'^del/$', 'unsubscribe', name='subscribe_delete'),
    url(r'^process/$', 'send_notifications', name='subscribe_process'),
)
