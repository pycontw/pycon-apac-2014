from django.db import models
from django.utils.translation import ugettext_lazy as _


class ReviewRecordModel(models.Model):

    RANK_CHOICES = (
        (-3, -3),
        (-2, -2),
        (-1, -1),
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3)
    )

    proposal = models.ForeignKey("proposal.ProposalModel")
    reviewer = models.ForeignKey("auth.User")
    rank = models.IntegerField(verbose_name=_("Rank"), default=0,
                               choices=RANK_CHOICES)
    comment = models.TextField(verbose_name=_("Comment"),
                               blank=False, null=True)


class ProposalResultModel(models.Model):

    RESULT_CHOICES = (
        (-1, "Rejected"),
        (0, "Undecided"),
        (1, "Accepted")
    )

    proposal = models.OneToOneField("proposal.ProposalModel", related_name="result")
    decision = models.IntegerField(verbose_name=_("Decision"), default=0,
                                   choices=RESULT_CHOICES)
    referee = models.ForeignKey("auth.User", null=True)
