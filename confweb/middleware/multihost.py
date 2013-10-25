##
# A middleware which set "SITE_ID" according to current language
##

from django.conf import settings
from django.utils import translation
from django.core.urlresolvers import resolve
from django.contrib.sites.models import Site


def is_supported_language(lang_code):
    return lang_code in [lang[0] for lang in settings.LANGUAGES]


def get_no_lang_path(request):
    pieces = request.path.split('/', 2)
    lang_code = pieces[1]
    if is_supported_language(lang_code):
        return pieces[2] if len(pieces) > 2 else '/'
    else:
        return request.path


class MultiHostMiddleware:

    def process_view(self, request, view_func, view_args, view_kwargs):
        try:
            request.no_lang_path = get_no_lang_path(request)

            if request.path.find("/set_site") != -1:
                site_id = request.GET["site_id"]
                site = Site.objects.get(id=site_id)
                request.session['django_language'] = site.name

            if not resolve(request.path).namespace == "admin":
                site_lang = translation.get_language()
                site = Site.objects.get(name=site_lang)
                request.session['site_id'] = site.id

        except Exception as inst:
            print inst
            request.session['site_id'] = settings.SITE_ID
