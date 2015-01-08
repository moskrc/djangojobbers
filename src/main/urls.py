from django.conf.urls import patterns, include, url
from django.contrib import admin
from catalog.feeds import LatestEntriesFeed

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'catalog.views.index', name='home'),
    url(r'^catalog/', include('catalog.urls')),
    url(r'^subscription/', include('subscription.urls')),
    url(r'^feedback/', include('feedback.urls')),
    url(r'^feed/$', LatestEntriesFeed()),
    url(r'^admin/', include(admin.site.urls)),
)
