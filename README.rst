django-featured-objects
=======================

Simple Django app for making any object featured.

Authored by `Pedro Burón <http://pedroburon.info/>`_, and some great
`contributors <https://github.com/bashu/django-featured-objects-redux/contributors>`_.

.. image:: https://img.shields.io/pypi/v/django-featured-objects-redux.svg
    :target: https://pypi.python.org/pypi/django-featured-objects-redux/

.. image:: https://img.shields.io/pypi/dm/django-featured-objects-redux.svg
    :target: https://pypi.python.org/pypi/django-featured-objects-redux/

.. image:: https://img.shields.io/github/license/bashu/django-featured-objects-redux.svg
    :target: https://pypi.python.org/pypi/django-featured-objects-redux/

.. image:: https://img.shields.io/travis/bashu/django-featured-objects-redux.svg
    :target: https://travis-ci.org/bashu/django-featured-objects-redux/


Installation
============

First install the module, preferably in a virtual environment. It can be installed from PyPI:

.. code-block:: shell

    pip install django-featured-objects-redux

Setup
=====

You'll need to add ``featured_objects`` to ``INSTALLED_APPS`` in your project's ``settings.py`` file:

.. code-block:: python

    INSTALLED_APPS += [
        'featured_objects',
    ]

Then run ``./manage.py migrate`` to create the required database tables.

Configuration
=============

There is only one mandatory configuration option you need to set in your ``settings.py`` :

.. code-block:: python

    FEATURABLE_MODELS = (
        ('app_label', 'model_name'), 
        ('app_label', 'another_model_name'),
    )

Usage
=====
[TBD]

Contributing
------------

If you've found a bug, implemented a feature or customized the template and
think it is useful then please consider contributing. Patches, pull requests or
just suggestions are welcome!

License
-------

``django-featured-objects-redux`` is released under the GPLv3 license.

.. _django: https://www.djangoproject.com
