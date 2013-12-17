from django.db import models
from django.utils.translation import ugettext as _


class UserProfile(models.Model):
    user = models.OneToOneField("auth.User")
    brief = models.TextField(
        verbose_name=_("Speaker Brief"),
        null=True, blank=True)
    tagline = models.CharField(
        max_length=64,
        verbose_name=_("Tagline: split by comma. E.g. pycontw, IPython, pep8"),
        null=True, blank=True)
    location = models.CharField(
        max_length=128,
        verbose_name=_("Location"),
        null=True, blank=True)
    personal_url = models.URLField(verbose_name=_("Personal Link"),
                                   null=True, blank=True)
    twitter_username = models.CharField(
        max_length=64,
        verbose_name=_("Twitter Username"),
        null=True, blank=True)
    org = models.CharField(
        max_length=128,
        verbose_name=_("Organization/Company"),
        null=True, blank=True)
    org_url = models.URLField(verbose_name=_("Link of Organization/Companyk"),
                              null=True, blank=True)
    title = models.CharField(
        max_length=128,
        verbose_name=_("Title"),
        null=True, blank=True)
    picture = models.ImageField(verbose_name=_("Picture"),
                                upload_to="picture", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
