from django.conf.urls import patterns, include, url

urlpatterns = patterns("proposal_review.views",
                       url('^review/(\d+)/$', 'do_review', name='do_review'),
                       url('^decision/(\d+)/$', 'make_decision', name='make_decision'),
                       url('^proposals/$', 'list_proposals', name='list_proposals'),
                       url('^my_review/$', 'list_reviews', name='my_review', kwargs={"me": True}),
                       # url('^update/(\d+)/$', 'update_proposal', name='update'),
                       # url('^delete/(\d+)/$', 'delete_proposal', name='delete'),
                       )
