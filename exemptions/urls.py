from django.conf.urls import patterns, include, url

from exemptions.views import host as host_views
from exemptions.views import exemption as exemption_views
from exemptions.views import user as user_views

host_urls = patterns('',
  url(r'^$', host_views.HostList.as_view(), name='host_list'),
  url(r'^new$', host_views.HostCreate.as_view(), name='host_new'),
  url(r'^edit/(?P<pk>\d+)$', host_views.HostUpdate.as_view(), name='host_edit'),
  url(r'^delete/(?P<pk>\d+)$', host_views.HostDelete.as_view(), name='host_delete'),
)

exemption_urls = patterns('',
  url(r'^$', exemption_views.ExemptionList.as_view(), name='exemption_list'),
  url(r'^new$', exemption_views.ExemptionCreate.as_view(), name='exemption_new'),
  url(r'^edit/(?P<pk>\d+)$', exemption_views.ExemptionUpdate.as_view(), name='exemption_edit'),
  url(r'^delete/(?P<pk>\d+)$', exemption_views.ExemptionDelete.as_view(), name='exemption_delete'),
)

user_urls = patterns('',
  url(r'^$', user_views.UserList.as_view(), name='user_list'),
  url(r'^new$', user_views.UserCreate.as_view(), name='user_new'),
  url(r'^edit/(?P<pk>\d+)$', user_views.UserUpdate.as_view(), name='user_edit'),
  url(r'^delete/(?P<pk>\d+)$', user_views.UserDelete.as_view(), name='user_delete'),
)

urlpatterns = patterns('',
    url(r'^hosts/', include(host_urls)),
    url(r'^users/', include(user_urls)),
    url(r'', include(exemption_urls)),
)
