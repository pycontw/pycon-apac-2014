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
    comment = models.TextField(verbose_name=_("Comment"), blank=True, null=True)
