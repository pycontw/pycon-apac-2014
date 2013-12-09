import os
import subprocess
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


class in_virtualenv(object):
    "Used as decorator"
    def __init__(self, f, venv_prefix=VENV_PREFIX):
        self.f = f
        self.venv_prefix = venv_prefix

    def __call__(self, *args, **kwargs):
        with lcd("confweb"):
            with prefix('. %s/bin/activate' % self.venv_prefix):
                self.f(*args, **kwargs)


@in_virtualenv
def dumpdata(venv_prefix=VENV_PREFIX, output="dumpdata.json"):
    local("python manage.py dumpdata > {}{}{}".format(
        os.getcwd(), os.sep, output))


@in_virtualenv
def deploy(role):
    if role == "developer":
        local("python manage.py syncdb --noinput")
    elif role == "deployment":
        local("python manage.py syncdb --noinput")


@in_virtualenv
def shell(interface=""):
    cmd = "python manage.py shell"
    if interface:
        cmd += " -i {}".format(interface)
    local(cmd)


@in_virtualenv
def serve(host="0.0.0.0", port="8000"):
    if which('sass'):
        subprocess.Popen("sass --watch scss/all.scss:all.css".split(),
                         cwd='confweb/static/')
    local("python manage.py runserver {}:{}".format(host, port))


def which(program):
    # http://stackoverflow.com/a/377028
    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            path = path.strip('"')
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file

    return None
