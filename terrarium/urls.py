from django.conf.urls import include, url
from django.contrib import admin

from terrarium.core.views import HomeView
from terrarium.watchdog.views import CheckWatchdogsView


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^check-watchdogs/$', CheckWatchdogsView.as_view(), name='check-watchdogs'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('didadata.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
