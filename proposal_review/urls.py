from django.conf.urls import patterns, include, url

urlpatterns = patterns("proposal_review.views",
                       url('^create/(\d+)/$', 'create_review', name='create_review'),
                       url('^list/$', 'list_proposals', name='list_proposals'),
                       # url('^update/(\d+)/$', 'update_proposal', name='update'),
                       # url('^delete/(\d+)/$', 'delete_proposal', name='delete'),
                       )
