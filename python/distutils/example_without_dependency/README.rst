=============
DistutilsDemo
=============

Copyright (c) 2015,2016 Jeremie DECOCK (http://www.jdhp.org)


Description
===========

This snippet was written to test distutils and PyPI.
It is inspired by `this tutorial`_.


Dependencies
============

- Python >= 3.0


Install
=======

This demo can be installed with Python Distutils by entering the following command
in a terminal::

    python3 setup.py install

.. _install:

Installation
============

Gnu/Linux
---------

You can install, upgrade, uninstall this demo with these commands
(in a terminal)::

    pip install --pre jdhp-distutils-demo
    pip install --upgrade jdhp-distutils-demo
    pip uninstall jdhp-distutils-demo

Or, if you have downloaded the source code::

    python3 setup.py install

Windows
-------

You can install, upgrade, uninstall this demo with these commands
(in a `command prompt`_)::

    py -m pip install --pre jdhp-distutils-demo
    py -m pip install --upgrade jdhp-distutils-demo
    py -m pip uninstall jdhp-distutils-demo

Or, if you have downloaded the source code::

    py setup.py install

MacOSX
-------

You can install, upgrade, uninstall this demo with these commands
commands (in a terminal)::

    pip install --pre jdhp-distutils-demo
    pip install --upgrade jdhp-distutils-demo
    pip uninstall jdhp-distutils-demo

Or, if you have downloaded the source code::

    python3 setup.py install


Usage
=====

Usage::

    from jdhp_distutils_demo import row_your_boat
    row_your_boat.sing()


License
=======

This demo is distributed under the `MIT License`_

.. _this tutorial: http://sametmax.com/creer-un-setup-py-et-mettre-sa-bibliotheque-python-en-ligne-sur-pypi/
.. _MIT License: http://opensource.org/licenses/MIT
