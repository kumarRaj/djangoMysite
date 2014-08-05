from django.conf.urls import patterns, include, url

from django.contrib import admin
from mysite.views import *
admin.autodiscover()



urlpatterns = patterns('',
    # Examples:
    url(r'^time/plus/(\d{1,5})/$', hours_ahead),
    url(r'^time/$', current_datetime),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    url(r'',hello)
)

