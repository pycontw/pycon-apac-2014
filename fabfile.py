from fabric.api import local, run, env, put, sudo, cd, lcd, settings, prefix
import os

# env.hosts = ["127.0.0.1"]
# env.user = "test"
# env.password = "qwerty"

def create_virtualenv(venv_name=".virtualenvs"):
    local('virtualenv %s' % venv_name)
    with prefix('source %s/bin/activate' % venv_name):
        with settings(warn_only=True):
            local('pip install -r requirements/project.txt')


def deploy(role, venv_name=".virtualenvs"):
    with lcd("confweb"):
        with prefix('source ../%s/bin/activate' % venv_name):
            if role == "developer":
                local("python manage.py syncdb --noinput")
            elif role == "deployment":
                local("python manage.py syncdb --noinput")


def runserver(port="8000", venv_name=".virtualenvs"):
    with lcd("confweb"):
        with prefix('source ../%s/bin/activate' % venv_name):
            local("python manage.py runserver %s" % port)
