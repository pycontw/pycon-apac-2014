from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


class UserProfile(models.Model):
    user = models.OneToOneField("auth.User")
    brief = models.TextField(
        verbose_name=_("Speaker Brief"),
        null=True, blank=True)
    tagline = models.CharField(
        max_length=64,
        verbose_name=_("Tagline: split by comma."),
        help_text=_("e.g., pycontw, IPython, pep8"),
        null=True, blank=True)
    location = models.CharField(
        max_length=128,
        verbose_name=_("Location"),
        help_text=_("i.e. where you from?"),
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
    org_url = models.URLField(verbose_name=_("Link of Organization/Company"),
                              null=True, blank=True)
    title = models.CharField(
        max_length=128,
        verbose_name=_("Title"),
        null=True, blank=True)
    picture = models.ImageField(verbose_name=_("Picture"),
                                upload_to="picture", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    @property
    def is_reviewer(self):
        group_name = getattr(settings, "REVIEWER_GROUP_NAME", "Reviewer")
        return self.user.groups.filter(name=group_name).count()
