from django.core import mail
from django.conf import settings


class Mailer(object):

    sender = settings.EMAIL_HOST_USER

    @classmethod
    def send_to(Cls, receivers, subject, content, bcc=[]):
        email = mail.EmailMessage(subject, content, Cls.sender, receivers, bcc)
        email.send()
