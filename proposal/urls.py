
from django.conf.urls import patterns, include, url

urlpatterns = patterns("proposal.views",
                       url('^create/$', 'create_proposal', name='create'),
                       url('^list/$', 'list_proposal', name='list'),
                       url('^update/(\d+)/$', 'update_proposal', name='update'),
                       url('^delete/(\d+)/$', 'delete_proposal', name='delete'),
                       )
