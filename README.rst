===============
PyCon APAC 2014
===============

This repository serves the website of PyCon APAC 2024.
This project is open source and the license can be found in LICENSE.


Getting Started
---------------

Requirements
~~~~~~~~~~~~

 * Git 1.8+
 * Python 2.7+

Setting up environment
~~~~~~~~~~~~~~~~~~~~~~

Clone this repository::

    $ git clone git@bitbucket.org:pycontw/pycon-apac-2014.git

Setup its virtualenv and requirements through fabric script:

    $ cd pycon-apac-2014
    $ python scripts/bootstrap_dev.py

Running a web server
--------------------

In development you should run::

    $ source .virtualenvs/pythontw/bin/activate
    $ fab runserver

This will run a web server with default port, 8000. If you want to run the
server in a specific port:

    $ fab runserver:8090
