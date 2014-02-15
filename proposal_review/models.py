from django.db import models
from django.utils.translation import ugettext_lazy as _


class ReviewRecordModel(models.Model):

    proposal = models.ForeignKey("proposal.ProposalModel")
    reviewer = models.ForeignKey("auth.User")
    rank = models.PositiveIntegerField(verbose_name=_("Rank"), default=0)
    comment = models.TextField(verbose_name=_("Comment"))
