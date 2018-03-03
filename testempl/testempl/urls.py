from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
import emplmod
from emplmod import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testempl.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^emplog/',views.loginauth),
    url(r'^templates/(?P<path>.*)$', 'django.views.static.serve',  {'document_root': 'C:/Python27/testempl/emplmod/templates/'}),

)
