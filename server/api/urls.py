from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'server.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^amb/$', 'api.views.amb', name='api'),
    url(r'^reg/$', 'api.views.reg', name='reg'),
    url(r'^shake/$', 'api.views.shake', name='shake'),
    url(r'^upd/$', 'api.views.findhandshakes', name='cron'),
    url(r'^req/$', 'api.views.req', name='possible'),
    url(r'^fin/$', 'api.views.fin', name='final'),
)
