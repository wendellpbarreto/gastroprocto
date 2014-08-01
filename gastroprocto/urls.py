from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from gastroprocto.apps.gui.views import GUIView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', RedirectView.as_view(url='/home/')),

    url(r'^(?P<slug>\w+)/$', GUIView.as_view(), name='gui',),
    url(r'^(?P<slug>\w+)/(?P<pk>\d+)$', GUIView.as_view(), name='gui',),

)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()