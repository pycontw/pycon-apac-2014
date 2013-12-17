import os
import subprocess
from fabric.api import (
    local,
    run,
    env,
    roles,
    #put,
    #sudo,
    cd,
    lcd,
    #settings,
    prefix,
    execute
)

from scripts.make_virtualenv import get_venv_prefix


def config_fabric(local_settings={}):
    env.roledefs['web'] = []
    roledefs = local_settings.get('roledefs', {})
    for role, hostlist in roledefs.items():
        print("Setting hosts role '{}': {}".format(role, hostlist))
        env.roledefs[role] = hostlist


local_settings = {}


def load_fabric_settings(settings_module='local_fabric'):
    global local_settings
    if os.path.exists(settings_module + ".py"):
        local_fabric = __import__(settings_module)
        local_settings = local_fabric.settings
    config_fabric(local_settings)


load_fabric_settings()
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
        with lcd("conweb"):
            with prefix('. %s/bin/activate' % self.venv_prefix):
                self.f(*args, **kwargs)


@in_virtualenv
def setup():
    local("pip install -r ../requirements/project.txt")


@in_virtualenv
def local_deploy():
    local("python manage.py syncdb --noinput")


@roles('web')
def remote_deploy():
    repo_path = local_settings['repo_path']
    with cd(repo_path):
        run('git pull')
        run('supervisorctl restart pycon')


def deploy(target=""):
    if target in ("", "developer"):
        execute(local_deploy)
    elif target == "production":
        execute(remote_deploy)


@in_virtualenv
def serve(host="0.0.0.0", port="8000"):
    if which('sass'):
        subprocess.Popen("sass --watch scss/all.scss:all.css",
                         shell=True,
                         cwd='conweb/static/')
    if which('coffee'):
        subprocess.Popen("coffee --join all.js --watch"
                         " --compile coffees/app.coffee",
                         shell=True,
                         cwd='conweb/static/')
    local("python manage.py runserver {}:{}".format(host, port))


@in_virtualenv
def shell(interface=""):
    cmd = "python manage.py shell"
    if interface:
        cmd += " -i {}".format(interface)
    local(cmd)


@in_virtualenv
def dumpdata(venv_prefix=VENV_PREFIX, output="dumpdata.json"):
    local("python manage.py dumpdata > {}{}{}".format(
        os.getcwd(), os.sep, output))


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
