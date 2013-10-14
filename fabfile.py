import os
from fabric.api import (
    local,
    #run,
    #env,
    #put,
    #sudo,
    #cd,
    lcd,
    #settings,
    prefix
)

from scripts.make_virtualenv import get_venv_prefix


# env.hosts = ["127.0.0.1"]
# env.user = "test"
# env.password = "qwerty"


VENV_PREFIX = get_venv_prefix()


def dumpdata(venv_prefix=VENV_PREFIX, output="dumpdata.json"):
    with lcd("confweb"):
        with prefix('. %s/bin/activate' % venv_prefix):
            local("python manage.py dumpdata > {}{}{}".format(
                os.getcwd(), os.sep, output))


def deploy(role, venv_prefix=VENV_PREFIX):
    with lcd("confweb"):
        with prefix('. %s/bin/activate' % venv_prefix):
            if role == "developer":
                local("python manage.py syncdb --noinput")
            elif role == "deployment":
                local("python manage.py syncdb --noinput")


def runserver(port="8000", venv_prefix=VENV_PREFIX):
    with lcd("confweb"):
        with prefix('. %s/bin/activate' % venv_prefix):
            local("python manage.py runserver %s" % port)
