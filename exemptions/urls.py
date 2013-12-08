from django.conf.urls import patterns, include, url

from exemptions.views import host as host_views
from exemptions.views import exemption as exemption_views
from exemptions.views import authority as authority_views

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

authority_urls = patterns('',
  url(r'^$', authority_views.AuthorityList.as_view(), name='authority_list'),
  url(r'^new$', authority_views.AuthorityCreate.as_view(), name='authority_new'),
  url(r'^edit/(?P<pk>\d+)$', authority_views.AuthorityUpdate.as_view(), name='authority_edit'),
  url(r'^delete/(?P<pk>\d+)$', authority_views.AuthorityDelete.as_view(), name='authority_delete'),
)

urlpatterns = patterns('',
    url(r'^hosts/', include(host_urls)),
    url(r'^authorities/', include(authority_urls)),
    url(r'', include(exemption_urls)),
)
