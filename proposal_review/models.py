from django.db import models
from django.utils.translation import ugettext_lazy as _


class ReviewRecordModel(models.Model):

    RANK_CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    )

    proposal = models.ForeignKey("proposal.ProposalModel")
    reviewer = models.ForeignKey("auth.User")
    rank = models.PositiveIntegerField(verbose_name=_("Rank"), default=0,
                                       choices=RANK_CHOICES)
    comment = models.TextField(verbose_name=_("Comment"), blank=True, null=True)
