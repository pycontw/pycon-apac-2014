from django import http
from django.utils import translation
from django.utils.http import is_safe_url
from django.utils.translation import check_for_language
from django.conf import settings


def set_language(request):
    """
    Rewrite django.views.i18n.set_language by using lang_code in domain
    """
    site_lang = translation.get_language()
    url_lang_prefix = '/{}/'.format(site_lang)
    next = request.REQUEST.get('next')
    if not is_safe_url(url=next, host=request.get_host()):
        next = request.META.get('HTTP_REFERER')
        if not is_safe_url(url=next, host=request.get_host()):
            next = url_lang_prefix
        else:
            for lang_code, __ in settings.LANGUAGES:
                if next.find('/{}/'.format(lang_code)) != -1:
                    url_lang_prefix = '/{}/'.format(lang_code)
                    break

    response = None
    lang_code = request.GET.get('language', None)
    if lang_code and check_for_language(lang_code):
        next = next.replace(url_lang_prefix, '/{}/'.format(lang_code))
        if hasattr(request, 'session'):
            request.session['django_language'] = lang_code
        else:
            response = http.HttpResponseRedirect(next)
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)
    return response or http.HttpResponseRedirect(next)
