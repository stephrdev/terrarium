from django.conf.urls import include, url
from django.contrib import admin

from terrarium.core.views import HomeView, RecordsApiView


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('didadata.urls')),
    url(r'^api2/records/', RecordsApiView.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
