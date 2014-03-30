from django.conf.urls import patterns, include, url

urlpatterns = patterns("speaker.views",
                       url('^$', 'list_speakers', name='list'),
                       )
