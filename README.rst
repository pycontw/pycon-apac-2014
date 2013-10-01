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

Setting up environment
~~~~~~~~~~~~~~~~~~~~~~

Create a virtual environment where pycontw dependencies will live::

    $ virtualenv pycontw
    $ source pycontw/bin/activate
    (pycontw)$

Clone this repository::

    (pycontw)$ cd pycontw
    (pycontw)$ git clone git@bitbucket.org:pycontw/pycon-apac-2014.git

Install project dependencies::

    (pycontw)$ cd pycon-apac-2014
    (pycontw)$ pip install -r requirements/project.txt

Setting up the database
-----------------------

This will vary for production and development. By default the project is set
up to run on a SQLite database. If you are setting up a production database
see the Configuration section below for where to place settings and get the
database running. Now you can run::

    (pycontw)$ python confweb/manage.py createdb

Running a web server
--------------------

In development you should run::

    (pycontw)$ cd confweb
    (pycontw)$ python manage.py runserver
