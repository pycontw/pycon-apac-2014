from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Reset password of local admin to "develop"'

    def handle(self, *args, **options):
        ADMIN = {
            'username': 'admin',
            'email': 'dev@pycon.tw',
            'password': 'develop'
        }

        username, email, password = \
            ADMIN['username'], ADMIN['email'], ADMIN['password']
        user = User.objects.get(username__exact=username)
        if not user:
            print('Superuser created:', username)
            User.objects.create_superuser(username, email, password)
        else:
            user.set_password(password)
            user.save()
