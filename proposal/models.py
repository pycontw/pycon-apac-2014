from django.db import models
from django.utils.translation import ugettext_lazy as _z


class ProposalModel(models.Model):

    LANGUAGE_CHOICES = (
        (0, _z("English")),
        (1, _z("Mandarin")),
    )

    SPEECH_TYPE_CHOICES = (
        (0, _z("Regular Talk")),
        (1, _z("Lightning Talk")),
        (2, _z("SciPy Talk")),
        (3, _z("Tutorial")),
    )

    LEVEL_CHOICES = (
        (0, _z("Beginner")),
        (1, _z("Advanced")),
        (2, _z("Expert")),
        (3, _z("Scientific Background")),
    )

    TALK_PERMISSION_CHOICES = (
        (0, _z("Don't record my talk")),
        (1, _z("CC-BY-NC-SA")),
    )

    SLIDE_PERMISSION_CHOICES = (
        (0, _z("Don't publish my slide")),
        (1, _z("CC-BY-NC-SA")),
    )

    title = models.CharField(verbose_name=_z("Title"),
                             help_text=_z("Title of the talk or tutorial"),
                             max_length=100)
    author = models.ForeignKey("auth.User")
    speech_type = models.IntegerField(verbose_name=_z("Type of the proposal"),
                                      choices=SPEECH_TYPE_CHOICES)
    language = models.IntegerField(
        verbose_name=_z("Language"),
        choices=LANGUAGE_CHOICES,
        help_text=_z("SciPy Talk accepts only English")
    )
    audience_level = models.IntegerField(verbose_name=_z("Audience level"),
                                         choices=LEVEL_CHOICES)
    talk_perm = models.IntegerField(
        choices=TALK_PERMISSION_CHOICES,
        verbose_name=_z(
            "Permission for your talk to be recorded "
            "and released on the conference website"),
    )
    slide_perm = models.IntegerField(
        choices=SLIDE_PERMISSION_CHOICES, null=True, blank=True,
        verbose_name=_z(
            "Permission for your presentation slide to"
            " be downloaded from the conference website"),
    )
    description = models.TextField(
        verbose_name=_z("Description"),
        help_text=_z("Abstract or outline of your presentation. ")
    )
    additional_info = models.TextField(
        verbose_name=_z("Additional information"), null=True, blank=True,
        help_text=_z("Additional information that can help the program"
                     " committee to make decisions (e.g., years of experie)")
    )
    create_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)


class AbstractFile(models.Model):
    proposal = models.OneToOneField(ProposalModel)
    abstract = models.FileField(verbose_name=_z("Abstract"),
                                upload_to="abstract", null=True, blank=True)

    @property
    def has_file(self):
        return bool(self.abstract)

    def url(self):
        # Shortcuts of file url.
        return self.abstract.url if self.has_file else ""

    def __unicode__z(self):
        return self.abstract.name.split('/')[-1] if self.has_file else ""
