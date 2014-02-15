from django.conf.urls import patterns, include, url

urlpatterns = patterns("proposal_review.views",
                       url('^create/(\d+)/$', 'do_review', name='do_review'),
                       url('^proposals/$', 'list_proposals', name='list_proposals'),
                       # url('^update/(\d+)/$', 'update_proposal', name='update'),
                       # url('^delete/(\d+)/$', 'delete_proposal', name='delete'),
                       )
