===============
PyCon APAC 2014
===============

This repository serves the website of PyCon APAC 2014.
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
    $ cd pycon-apac-2014

Setup its virtualenv and requirements::

    $ python scripts/make_virtualenv.py .venv

Which will create a default virtualenv path ".venv" inside pycon-apac-2014
folder.

Then install the required packages in this virtualenv (.venv)::

    $ .venv/bin/pip install -r requirements/project.txt


Setting up the database
-----------------------

This will vary for production and development. By default the project is set
up to run on a SQLite database. If you are setting up a production database
see the Configuration section below for where to place settings and get the
database running. Now you can run::

    $ .venv/bin/fab deploy:developer

For deployment of testing or production::

    $ .venv/bin/fab deploy:deployment

Running a web server
--------------------

In development you should run::

    $ .venv/bin/fab runserver

This will run a web server with default port, 8000. If you want to run the
server in a specific port::

    $ .venv/bin/fab runserver:8090


For Python developers
---------------------

Question about ".venv/bin/fab"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Can I use ``fab ...`` without virtualenv prefix ".venv/bin/"?  It's annoying.

Answer
~~~~~~

Yes you can. Activate installed virtualenv like
``source .venv/bin/activate``. There you can go with ``fab`` commands.

Or, if you already have fabric installed system-wide, you can just run
``fab ...`` without virtualenv prefix path needed.

Question about my favor of virtualenv
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Can I use my favor of virtualenv version and path?
e.g. (~/.virtualenvs/pycontw)

Answer
~~~~~~

Yes you can. Create a file named "venv_prefix" inside pycon-apac-2014
folder and put (or replace) your own created virtualenv path in first line.
The example of file content::

    ~/.virtualenvs/pycontw

You will need to replace above virtualenv prefix ``.venv/bin/*`` with
``{your_virutalenv_path}/bin/*``; or source your virtualenv before hand.


How to contribute
-----------------

Everyone who desires to improve the pycon-apac-2014 website can involve it
by the following working flow.

Fork on Bitbucket
~~~~~~~~~~~~~~~~~

First, you have to fork this repository::

    `Fork it on pycontw<https://bitbucket.org/pycontw/pycon-apac-2014/fork>`_

Then, clone the repository which you has forked::

    $ git clone git@bitbucket.org:<your_bitbucket_id>/pycon-apac-2014.git

Follow the steps of getting started on the top of the tutorial to setup
your environment.

Create a new branch
~~~~~~~~~~~~~~~~~~~

It is a good practice to generate a new branch for the new feature or
bugs that you want to fix. The branch name is not restricted but a
related name is prefered. You can create a branch by::

    $ git checkout master -b <branch_name>

Submit a pull-request
~~~~~~~~~~~~~~~~~~~~~

After you had finished your patch and committed the new branch onto your
repository, you could submit a pull-request onto "pycontw/pycon-apac-2014".

You can find the button on the top-left of you repository page on Bitbucket.

Gotcha
~~~~~~

Q: The master had updated and conflicted with my pull-request?
==============================================================

You need to rebase your repositary on to the origin/master

    $ git pull --rebase origin/master

After you updated and pushed your commit, you will need to click "Update"
on the pull-request which you had posted on Bitbucket.
