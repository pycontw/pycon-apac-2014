from django.db import models
from django.utils.translation import ugettext_lazy as _


class ProposalModel(models.Model):

    LANGUAGE_CHOICES = (
        (0, _("English")),
        (1, _("Mandarin")),
    )

    SPEECH_TYPE_CHOICES = (
        (0, _("Regular Talk")),
        (1, _("Lightning Talk")),
        (2, _("SciPy Talk")),
        (3, _("Tutorial")),
    )

    LEVEL_CHOICES = (
        (0, _("Beginner")),
        (1, _("Advanced")),
        (2, _("Expert")),
        (3, _("Scientific Background")),
    )

    TALK_PERMISSION_CHOICES = (
        (1, _("CC-BY-NC-SA")),
        (0, _("Don't record my talk")),
    )

    SLIDE_PERMISSION_CHOICES = (
        (1, _("CC-BY-NC-SA")),
        (0, _("Don't publish my slide")),
    )

    title = models.CharField(verbose_name=_("Title"),
                             help_text=_("Title of the talk or tutorial"),
                             max_length=100)
    author = models.ForeignKey("auth.User", related_name="proposals")
    speech_type = models.IntegerField(verbose_name=_("Type of the proposal"),
                                      choices=SPEECH_TYPE_CHOICES)
    language = models.IntegerField(
        verbose_name=_("Language"),
        choices=LANGUAGE_CHOICES,
        help_text=_("SciPy Talk accepts only English")
    )
    audience_level = models.IntegerField(verbose_name=_("Audience level"),
                                         choices=LEVEL_CHOICES)
    talk_perm = models.IntegerField(
        choices=TALK_PERMISSION_CHOICES,
        verbose_name=_(
            "Permission for your talk to be recorded "
            "and released on the conference website"),
    )
    slide_perm = models.IntegerField(
        choices=SLIDE_PERMISSION_CHOICES, null=True, blank=True,
        verbose_name=_(
            "Permission for your presentation slide to"
            " be downloaded from the conference website"),
    )
    description = models.TextField(
        verbose_name=_("Description"),
        help_text=_("Abstract or outline of your presentation. ")
    )
    additional_info = models.TextField(
        verbose_name=_("Additional information"), null=True, blank=True,
        help_text=_("Additional information that can help the program"
                    " committee to make decisions (e.g., years of experie)")
    )
    create_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    slide_link = models.URLField(null=True, blank=True)
    video_link = models.URLField(null=True, blank=True)

class AbstractFile(models.Model):
    proposal = models.OneToOneField(ProposalModel)
    abstract = models.FileField(verbose_name=_("Abstract"),
                                upload_to="abstract", null=True, blank=True)

    @property
    def has_file(self):
        return bool(self.abstract)

    def url(self):
        # Shortcuts of file url.
        return self.abstract.url if self.has_file else ""

    def __unicode__(self):
        return self.abstract.name.split('/')[-1] if self.has_file else ""
