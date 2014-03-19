from django.contrib.auth.models import User
from django.conf import settings

from conweb.lib.mailer import Mailer


def send_proposal_changed_notification(proposal):
    subject = u'Proposal Changed: {}'.format(proposal.title)
    content = "https://tw.pycon.org/proposal_review/review/{}".format(
        proposal.id)
    receivers = {review.reviewer.email
                 for review in proposal.reviewrecordmodel_set.all()}
    for useranme in settings.REVIEWER_ADMINS:
        review_admin = User.objects.get(username__exact=useranme)
        receivers.add(review_admin.email)
    Mailer.send_to(receivers, subject, content)
