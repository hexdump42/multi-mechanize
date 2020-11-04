
================================================
    Multi-Mechanize - Performance Test Framework
================================================

* Fork of Multi-Mechanize migrated to Py3k. Will not work with Python 2.
* Copyright: (c) 2010-2019 Corey Goldberg (cgoldberg _at_ gmail.com)
* 2020+ Changes: (c) 2020 Mark Rees (mark dot john dot rees _at_ gmail.com) & contributors 
* License: GNU LGPLv3
* Requires: Python 3.6+

----

:PyPI: `multi-mechanize <http://pypi.python.org/pypi/multi-mechanize>`_
:Dev: `git repo <http://github.com/hexdump42/multi-mechanize>`_

----

***********************
    Docs / Instructions
***********************

* https://github.com/hexdump42/multi-mechanize/blob/master/docs/README.rst

*******************
    Install / Setup
*******************

Multi-Mechanize can be installed from `PyPI <http://pypi.python.org/pypi/multi-mechanize>`_ using `pip <http://www.pip-installer.org>`_::
    
    pip install multi-mechanize

... or download the `source distribution from PyPI <http://pypi.python.org/pypi/multi-mechanize#downloads>`_, unarchive, and run::

    python setup.py install

... then use ``multimech-newproject`` and ``multimech-run`` to create and run your performance test projects.

****************************
    Detailed Install / Setup
****************************

These instructions are for Debian/Ubuntu Linux.  For other 
platforms, the setup is generally the same, with the exeption of 
installing system dependencies.  

-----------------------
    system-wide install
-----------------------

* install dependencies on Debian/Ubuntu::

    $ sudo apt-get install python-pip python-matplotlib
    
* install multi-mechanize from PyPI using Pip::

    $ sudo pip install -U multi-mechanize
    
* create a new project::

    $ multimech-newproject my_project

* run a project::

    $ multimech-run my_project

   
-------------------------------------------------------------
    virtualenv + pip install (with matplotlib system package)
-------------------------------------------------------------

* install dependencies on Debian/Ubuntu::

    $ sudo apt-get install python-virtualenv python-matplotlib

* install multi-mechanize from PyPI in a virtualenv::

    $ virtualenv --system-site-packages ENV
    $ cd ENV
    $ source bin/activate
    (ENV)$ pip install multi-mechanize
    
------------------------------------------------------
    virtualenv + pip install (with --no-site-packages)
------------------------------------------------------

* install dependencies on Debian/Ubuntu::

    $ sudo apt-get install build-essential libfreetype6-dev libpng-dev
    $ sudo apt-get install python-dev python-virtualenv

* install multi-mechanize and matplotlib from PyPI in a virtualenv::

    $ virtualenv ENV
    $ cd ENV
    $ source bin/activate
    (ENV)$ pip install multi-mechanize
    (ENV)$ pip install matplotlib

-----------------------------------------------
    pip install latest dev branch from git repo
-----------------------------------------------

::

    pip install -e git+http://github.com/cgoldberg/multi-mechanize.git#egg=multimechanize

