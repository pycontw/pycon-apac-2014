##
# A middleware which set "SITE_ID" according to current language
##

from django.conf import settings
from django.utils import translation
from django.core.urlresolvers import resolve
from django.contrib.sites.models import Site



class MultiHostMiddleware:

    def process_view(self, request, view_func, view_args, view_kwargs):
        try:
            if request.path_info.find("/set_site") != -1:
                site_id = request.GET["site_id"]
                site = Site.objects.get(id=site_id)
                request.session['django_language'] = site.name

            if not resolve(request.path_info).namespace == "admin":
                site_lang = translation.get_language()
                site = Site.objects.get(name=site_lang)
                request.session['site_id'] = site.id

        except Exception as inst:
            print inst
            request.session['site_id'] = settings.SITE_ID
