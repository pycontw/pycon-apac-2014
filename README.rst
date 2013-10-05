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
 * virtualenv 1.10.1+
 * fabric

Setting up environment
~~~~~~~~~~~~~~~~~~~~~~

Clone this repository::

    $ git clone git@bitbucket.org:pycontw/pycon-apac-2014.git

Setup its virtualenv and requirements through fabric script:

    $ cd pycon-apac-2014
    $ fab create_virtualenv

Setting up the database
-----------------------

This will vary for production and development. By default the project is set
up to run on a SQLite database. If you are setting up a production database
see the Configuration section below for where to place settings and get the
database running. Now you can run::

    $ fab deploy:deployment

For developer,

    $ fab deploy:developer

Running a web server
--------------------

In development you should run::

    $ fab runserver

This will run a web server with default port, 8000. If you want to run the
server in a specific port:

    $ fab runserver:8090
