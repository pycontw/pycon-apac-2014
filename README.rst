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
