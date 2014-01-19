import os
import subprocess
import functools

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

from scripts.make_virtualenv import get_venv_prefix as _get_venv_prefix


def _config_fabric(local_settings={}):
    env.roledefs['web'] = []
    roledefs = local_settings.get('roledefs', {})
    for role, hostlist in roledefs.items():
        print("Setting hosts role '{}': {}".format(role, hostlist))
        env.roledefs[role] = hostlist


local_settings = {}


def _load_fabric_settings(settings_module='local_fabric'):
    global local_settings
    if os.path.exists(settings_module + ".py"):
        local_fabric = __import__(settings_module)
        local_settings = local_fabric.settings
    _config_fabric(local_settings)


_load_fabric_settings()
# env.hosts = ["127.0.0.1"]
# env.user = "test"
# env.password = "qwerty"


VENV_PREFIX = _get_venv_prefix()
MY_APPS = ['proposal']
LANGUAGES = ('en', 'zh', 'ja')


def _in_virtualenv(wrapped):
    @functools.wraps(wrapped)
    def _wrapper(*args, **kwargs):
        with lcd("conweb"):
            with prefix('. %s/bin/activate' % VENV_PREFIX):
                return wrapped(*args, **kwargs)
    return _wrapper


def _print_ready_info(next_task=''):
    print("You're ready for `{}`".format(next_task))


@_in_virtualenv
def setup():
    "install project requirements"
    local("pip install -r ../requirements/project.txt")
    _print_ready_info('fab deploy')


@_in_virtualenv
def reset_password(username='admin'):
    "reset Django user password"
    local("python manage.py changepassword {}".format(username))


@_in_virtualenv
def translate(languages=LANGUAGES, compile_msg=False):
    "collect messages for translators"
    local("python manage.py makemessages -a")
    for app_name in MY_APPS:
        with lcd("../" + app_name):
            for lang in languages:
                local("django-admin.py makemessages -l " + lang)
    if compile_msg:
        execute(done_translate)


@_in_virtualenv
def done_translate(languages=LANGUAGES):
    "compile translated messages to make it show"
    local("python manage.py compilemessages")
    for app_name in MY_APPS:
        with lcd("../" + app_name):
            local("django-admin.py compilemessages")


@roles('web')
def _remote_copimlemessages(languages):
    "compile messages"
    repo_path = local_settings['repo_path']
    with cd(repo_path):
        run('fab done_translate')


@_in_virtualenv
def _local_deploy():
    "Django syncdb, migrate, and reset admin password"
    local("python manage.py syncdb --noinput")
    local("python manage.py migrate")
    local("python manage.py reset_admin_password")
    _print_ready_info('fab serve')


@roles('web')
def _remote_deploy():
    "update repository and restart web service"
    repo_path = local_settings['repo_path']
    with cd(repo_path):
        run('git pull')
        run('fab compilemessages')
        run('supervisorctl restart pycon')


def deploy(target=""):
    "in local: syncdb, migrate, and reset admin password"
    if target in ("", "developer"):
        execute(_local_deploy)
    elif target == "production":
        execute(_remote_deploy)


@_in_virtualenv
def serve(host="0.0.0.0", port="8000"):
    "i.e. start HTTP server default host 0.0.0.0 and port 8000"
    if _which('sass'):
        subprocess.Popen("sass --watch scss/all.scss:all.css",
                         shell=True,
                         cwd='conweb/static/')
    if _which('coffee'):
        subprocess.Popen("coffee --join all.js --watch"
                         " --compile coffees/app.coffee",
                         shell=True,
                         cwd='conweb/static/')
    local("python manage.py runserver {}:{}".format(host, port))


@_in_virtualenv
def shell(interface=""):
    "run Django shell"
    # NOTE: Ctrl-C will trigger fabric to interrupt shell
    cmd = "python manage.py shell"
    if interface:
        cmd += " -i {}".format(interface)
    local(cmd)


@_in_virtualenv
def dumpdata(output="dumpdata.json"):
    "dump Django databse data into JSON file"
    local("python manage.py dumpdata > {}{}{}".format(
        os.getcwd(), os.sep, output))


def _which(program):
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
