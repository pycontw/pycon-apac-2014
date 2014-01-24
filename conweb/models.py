from django.db import models
from django.utils.translation import ugettext_lazy as _z


class UserProfile(models.Model):
    user = models.OneToOneField("auth.User")
    brief = models.TextField(
        verbose_name=_z("Speaker Brief"),
        null=True, blank=True)
    tagline = models.CharField(
        max_length=64,
        verbose_name=_z("Tagline: split by comma."),
        help_text=_z("e.g., pycontw, IPython, pep8"),
        null=True, blank=True)
    location = models.CharField(
        max_length=128,
        verbose_name=_z("Location"),
        help_text=_z("i.e. where you from?"),
        null=True, blank=True)
    personal_url = models.URLField(verbose_name=_z("Personal Link"),
                                   null=True, blank=True)
    twitter_username = models.CharField(
        max_length=64,
        verbose_name=_z("Twitter Username"),
        null=True, blank=True)
    org = models.CharField(
        max_length=128,
        verbose_name=_z("Organization/Company"),
        null=True, blank=True)
    org_url = models.URLField(verbose_name=_z("Link of Organization/Company"),
                              null=True, blank=True)
    title = models.CharField(
        max_length=128,
        verbose_name=_z("Title"),
        null=True, blank=True)
    picture = models.ImageField(verbose_name=_z("Picture"),
                                upload_to="picture", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
