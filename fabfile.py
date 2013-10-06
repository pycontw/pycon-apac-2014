from fabric.api import (
    local,
    #run,
    #env,
    #put,
    #sudo,
    #cd,
    lcd,
    #settings,
    #prefix
)


# env.hosts = ["127.0.0.1"]
# env.user = "test"
# env.password = "qwerty"


def deploy(role):
    with lcd("confweb"):
        if role == "developer":
            local("python manage.py syncdb --noinput")
        elif role == "deployment":
            local("python manage.py syncdb --noinput")


def runserver(port="8000"):
    with lcd("confweb"):
        local("python manage.py runserver %s" % port)
