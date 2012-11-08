from django.conf.urls.defaults import patterns, include, url
import myapp.views 

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^myproject/', include('myproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^$', myapp.views.home),
    url(r'^mu-1bf8f3d4-b4e818d2-2e938574-5eb390f8.txt$', myapp.views.blitz),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
