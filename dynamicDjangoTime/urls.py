from django.conf.urls import patterns, include, url

from dynamicDjangoTime.views import AdamsFirstClass
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dynamicDjangoTime.views.home', name='home'),
    # url(r'^dynamicDjangoTime/', include('dynamicDjangoTime.foo.urls')),
	url(r'^time/$', AdamsFirstClass().current_time),
	url(r'^time/plus/(\d{1,2})/$', AdamsFirstClass().time_ahead),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
