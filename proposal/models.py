from django.db import models
from django.utils.translation import ugettext as _



class ProposalModel(models.Model):

    LANGUAGE_CHOICES = (
        (0, "English"),
        (1, "Mandarin"),
    )

    SPEECH_TYPE_CHOICES = (
        (0, "Regular Talk"),
        (1, "Lightning Talk"),
        (2, "SciPy Talk"),
        (3, "Tutorial"),
    )

    LEVEL_CHOICES= (
        (0, "Beginner"),
        (1, "Advanced"),
        (2, "Expert"),
        (3, "Scientific Background"),
    )

    TALK_PERMISSION_CHOICES = (
        (0, "Don't record my talk"),
        (1, "CC-BY-NC-SA"),
    )

    SLIDE_PERMISSION_CHOICES = (
        (0, "Don't record my talk"),
        (1, "CC-BY-NC-SA"),
    )

    title = models.CharField(verbose_name=_("Title"), max_length=100)
    author = models.ForeignKey("auth.User")
    speech_type = models.IntegerField(verbose_name=_("Type of the proposal"),
                                      choices=SPEECH_TYPE_CHOICES)
    language = models.IntegerField(verbose_name=_("Language"),
                                   choices=LANGUAGE_CHOICES)
    audience_level = models.IntegerField(verbose_name=_("Audience level"),
                                         choices=LEVEL_CHOICES)
    talk_perm = models.IntegerField(verbose_name=_("Talk Permission"),
                                    choices=TALK_PERMISSION_CHOICES)
    slide_perm = models.IntegerField(verbose_name=_("Slide Permission"),
                                     choices=SLIDE_PERMISSION_CHOICES)
    description = models.TextField(verbose_name=_("Description"))
    additional_info = models.TextField(
        verbose_name=_("Additional information"), null=True, blank=True)
    create_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)


class AbstractFile(models.Model):
    proposal = models.OneToOneField(ProposalModel)
    abstract = models.FileField(verbose_name=_("Abstract"),
                                upload_to="abstract", null=True, blank=True)

    def __unicode__(self):
        if self.abstract:
            return self.abstract.name
        else:
            return ""
