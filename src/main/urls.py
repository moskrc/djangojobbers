from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'catalog.views.index', name='home'),
    url(r'^catalog/', include('catalog.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
