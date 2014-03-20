from django.contrib.auth.models import User
from django.conf import settings

from conweb.lib.mailer import Mailer


def email_proposal_changed_task(proposal):
    subject = u'Proposal Changed: {}'.format(proposal.title)
    content = "https://tw.pycon.org/proposal_review/review/{}".format(
        proposal.id)
    receivers = {review.reviewer.email
                 for review in proposal.reviewrecordmodel_set.all()}
    bcc = set()
    for useranme in settings.REVIEWER_ADMINS:
        review_admin = User.objects.get(username__exact=useranme)
        if review_admin.email not in receivers:
            bcc.add(review_admin.email)
    Mailer.send_to(receivers, subject, content, bcc)
